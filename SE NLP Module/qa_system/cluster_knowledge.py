import xml.etree.ElementTree as ElementTree
import sys
import re
import string
import math
import numpy
import pickle
import os
import nltk
import json
import threading
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk import ne_chunk
from nltk.tree import Tree
from collections import Counter
from multiprocessing.dummy import Pool as ThreadPool
from tqdm import tqdm
from scipy.sparse import bsr_matrix
from glob import glob
from flask import Flask
from flask import request
from flask import Response
from flask import flash
from flask_cors import CORS
from werkzeug.utils import secure_filename

json_decoder = json.JSONDecoder()
json_encoder = json.JSONEncoder()

currently_creating_clusters = {}

stopWords = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
porterStemmer = PorterStemmer()
def CleanSentence(sentence, removeStopWords = True, addSynonyms = False):
	cleaned_sentence = []

	# preprocessing, could swap porter stemmer for wordnet lemmatizer
	words = word_tokenize(sentence)
	tagged_words = pos_tag(words)

	for word, pos in tagged_words:
		if word in string.punctuation:
			continue

		if removeStopWords and (word in stopWords):
			continue
		
		cleaned_sentence.append(porterStemmer.stem(word).lower())

		if addSynonyms:
			synonyms = [syn.name().split('.')[0] for syn in wordnet.synsets(word.lower())]
			cleaned_sentence += synonyms

	if addSynonyms:
		return list(set(cleaned_sentence))
	else:
		return cleaned_sentence


def create_clusters(topic_id, sentences, cleaned_sentences, similarityMatrix):

	global currently_creating_clusters

	currently_creating_clusters[topic_id] = {'changed': False, 'current_count': 0, 'max_count': (len(sentences) * (len(sentences) - 1) // 2)}

	clusters = []
	similarity_threshold = 0.5
	def SentenceSimilarity(t1, t2):
		vec1 = cleaned_sentences_with_counter[t1]
		vec2 = cleaned_sentences_with_counter[t2]

		intersection = set(vec1.keys()) & set(vec2.keys())
		numerator = sum(map(lambda x: vec1[x] * vec2[x], intersection))

		sum1 = sum(map(lambda x: vec1[x]**2, vec1.keys()))
		sum2 = sum(map(lambda x: vec2[x]**2, vec2.keys()))
		denominator = math.sqrt(sum1) * math.sqrt(sum2)

		cosine = 0.0 if (not denominator) else float(numerator) / denominator

		sentenceDistance = abs(int(t1) - int(t2))
		difference = 1 - (sentenceDistance / 10) if sentenceDistance < 10 else 0
		
		similarity = 0.5*cosine + 0.5*difference

		if (similarity > similarity_threshold):
			added = False
			for cluster in clusters:
				if t1 in cluster:
					added = True
					cluster.add(t2)
				elif t2 in cluster:
					added = True
					cluster.add(t1)
			else:
				if not added:
					clusters.append(set([t1, t2]))

		similarityMatrix[t1][t2] = similarity
		similarityMatrix[t2][t1] = similarity

		currently_creating_clusters[topic_id]['current_count'] += 1
		currently_creating_clusters[topic_id]['changed'] = True		

	cleaned_sentences_with_counter = [Counter(sentence) for sentence in cleaned_sentences]

	pool1 = ThreadPool()
	pool2 = ThreadPool()

	pool1.map(lambda x: pool2.map(lambda y: SentenceSimilarity(x,y), range(x+1, len(sentences))), range(len(sentences)-1))

	pool1.close()
	pool1.join()

	pool2.close()
	pool2.join()

	similarityMatrixSparse = bsr_matrix(similarityMatrix)

	clusters = [tuple(sorted(list(cluster))) for cluster in clusters]
	clusters = sorted(list(set(clusters)))

	del currently_creating_clusters[topic_id]

	return clusters

def extract_string_from_pdf(pdf_file):

	def StripHTMLTags(raw_html):
		cleaner = re.compile('<.*?>')
		cleantext = re.sub(cleaner, '', raw_html)

		return cleantext

	os.system("pdftohtml -xml \"" + pdf_file + "\" \"" + pdf_file + ".xml\" > /dev/null")

	string = ""

	tree = ElementTree.ElementTree(file = pdf_file + ".xml")
	root = tree.getroot()

	for element in root.getiterator():
		if (element.tag == 'text'):
			try:
				string += (" " + StripHTMLTags(element.text))
			except:
				pass

	return string

def extract_string_from_text(text_file): 
	return open(text_file, "r").read().replace('\n', ' ')

def entity_for_each_sentence(sent):
	chunked = ne_chunk(pos_tag(word_tokenize(sent)))
	prev = None
	continous_chunk = []
	current_chunk = []
	for i in chunked:
		if type(i) == Tree:
			current_chunk.append(" ".join([token for token, pos in i.leaves()]))
		elif current_chunk:
			named_entity = " ".join(current_chunk)
			if named_entity not in continous_chunk:
				continous_chunk.append(named_entity)
				current_chunk = []
		else:
			continue
	return continous_chunk

def train_bot(topic_id, string):

	
	sentences = sent_tokenize(string)
	cleaned_sentences = [CleanSentence(sentence) for sentence in sentences]

	similarityMatrix = numpy.zeros(shape = (len(sentences), len(sentences)))

	clusters = create_clusters(topic_id, sentences, cleaned_sentences, similarityMatrix)

	print(clusters)
	
	entity_all_sentences = list(map(lambda x: entity_for_each_sentence(x.lower()), sentences))
	for i in range(1,len(sentences)):
		entity_all_sentences[i] += entity_all_sentences[i-1]

	words = sorted(list(set([word for sentence in cleaned_sentences for word in sentence] + [word for sentence in entity_all_sentences for word in sentence])))

	search_matrix = numpy.zeros(shape = (len(clusters), len(words)))

	for i, cluster in enumerate(clusters):
		cluster_words = set([word for index in cluster for word in cleaned_sentences[index] + entity_all_sentences[index]])
		for word in cluster_words:
			search_matrix[i][words.index(word)] = 1

	search_matrix_sparse = bsr_matrix(search_matrix)
	similarity_matrix_sparse = bsr_matrix(similarityMatrix)

	fileObj = open(topic_id + '_Clusters', 'wb')
	pickle.dump(clusters, fileObj)
	fileObj.close()

	fileObj = open(topic_id + '_Sentences', 'wb')
	pickle.dump(sentences, fileObj)
	fileObj.close()

	fileObj = open(topic_id + '_Cleaned_Sentences', 'wb')
	pickle.dump(cleaned_sentences, fileObj)
	fileObj.close()

	fileObj = open(topic_id + '_Similarity_Matrix_Sparse', 'wb')
	pickle.dump(similarity_matrix_sparse, fileObj)
	fileObj.close()

	fileObj = open(topic_id + '_Important_Words', 'wb')
	pickle.dump(words, fileObj)
	fileObj.close()

	fileObj = open(topic_id + '_Search_Matrix_Sparse', 'wb')
	pickle.dump(search_matrix_sparse, fileObj)
	fileObj.close()


'''
@app.route("/upload_pdf", methods = ["POST"])
def upload_pdf():

	def allowed_file(filename):
		return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

	if 'file' not in request.files:
		return json_encoder.encode({"message":"Failure", "comment":"No file received"})

	file = request.files['file']
	
	if file.filename == '':
		return json_encoder.encode({"message":"Failure", "comment":"No file selected"})

	if file:
		if allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			
			string = extract_string_from_text(os.path.join(app.config['UPLOAD_FOLDER'], filename))

			threading.Thread(target = train_bot, args = (topic_id, string)).start()

			return json_encoder.encode({"message":"Success", "comment":"File uploaded successfully"})
		else:
			return json_encoder.encode({"message":"Failure", "comment":"File type not allowed"})

	return json_encoder.encode({"message":"Failure", "comment":"Internal Error"})

@app.route("/upload_txt", methods = ["POST"])
def upload_txt():

	def allowed_file(filename):
		return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

	if 'file' not in request.files:
		return json_encoder.encode({"message":"Failure", "comment":"No file received"})

	file = request.files['file']
	
	if file.filename == '':
		return json_encoder.encode({"message":"Failure", "comment":"No file selected"})

	if file:
		if allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			
			string = extract_string_from_text(os.path.join(app.config['UPLOAD_FOLDER'], filename))

			threading.Thread(target = train_bot, args = (topic_id, string)).start()

			return json_encoder.encode({"message":"Success", "comment":"File uploaded successfully"})
		else:
			return json_encoder.encode({"message":"Failure", "comment":"File type not allowed"})

	return json_encoder.encode({"message":"Failure", "comment":"Internal Error"})

@app.route("/upload_inputted_txt", methods = ["POST"])
def upload_inputted_txt():

	string = request.json['text']
	
	if len(string) == 0:
		return json_encoder.encode({"message":"Failure", "comment":"No text inputted."})

	threading.Thread(target = train_bot, args = (topic_id, string)).start()

	return json_encoder.encode({"message":"Success", "comment":"File uploaded successfully"})
			
@app.route("/get_clustering_progress/<json>", methods = ["GET"])
def get_clustering_progress(json):
	data = json_decoder.decode(json)
	topic_id = data['topic_id']

	if topic_id not in currently_creating_clusters:
		return json_encoder.encode({"message":"Failure", "comment":"No progress in creating clusters in this topic."})

	def get_clustering_progress_streamer():

		while True:

			if currently_creating_clusters[topic_id]['changed']:
				currently_creating_clusters[topic_id]['changed'] = False
				yield "event: CLUSTERING_PROGRESS\ndata: " + (currently_creating_clusters['current_count'] / currently_creating_clusters['max_count']) + "\n\n"

	return Response(get_clustering_progress_streamer(), mimetype = "text/event-stream")	
'''