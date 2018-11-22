import json
import os
import string
import numpy
import sys
import pickle
import scipy
import math
import nltk
import flask
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from textblob import TextBlob as tb
from flask import Flask
from flask import request
from flask import Response
from flask import flash
from flask_cors import CORS
from werkzeug.utils import secure_filename

json_decoder = json.JSONDecoder()
json_encoder = json.JSONEncoder()

#app = Flask(__name__)

#CORS(app)

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

def _answer_questions(passage, question, options):

	def TFIDF(sentences):

		def tf(word, blob):
			return blob.words.count(word) / len(blob.words)

		def n_containing(word, bloblist):
			return sum(1 for blob in bloblist if word in blob.words)

		def idf(word, bloblist):
			return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

		def tfidf(word, blob, bloblist):
			return tf(word, blob) * idf(word, bloblist)

		if type(sentences[0]) == type(list()):
			bloblist = [tb(" ".join(sentence)) for sentence in sentences]
		else:
			bloblist = [tb(sentence) for sentence in sentences]
		
		scores = [{word: tfidf(word, blob, bloblist) for word in blob.words} for i, blob in enumerate(bloblist)]

		return scores

	def SentenceSimilarities(sentences, tfidfScores, one_sentence, weighted = False):
			
		if (type(sentences[0]) != type(list())):
			for i in range(len(sentences)):
				sentences[i] = word_tokenize(sentences[i])

		if (type(one_sentence) != type(list())):
			one_sentence = word_tokenize(one_sentence)

		scores = []
		i = 0

		for sentence in sentences:
			current_score = 0
			for word in one_sentence:
				if word in sentence:
					if weighted == False:
						try:
							current_score += (1 * tfidfScores[i][word])
						except:
							pass
					else:
						try:
							current_score += (1 * tfidfScores[i][word]) * (1 / (1 + abs(i - weighted)))
						except:
							pass
			scores.append(current_score)
			i += 1

		return scores

	sentences_in_passage = sent_tokenize(passage)
	cleaned_sentences_in_passage = [CleanSentence(sentence) for sentence in sentences_in_passage]

	cleaned_sentences_without_removing_stopwords = [CleanSentence(sentence, removeStopWords = False) for sentence in sentences_in_passage]
	passage_sentence_scores = TFIDF(cleaned_sentences_without_removing_stopwords)

	answers = []

	choice_probabilities = []

	cleaned_question = CleanSentence(question)

	question_scores = SentenceSimilarities(cleaned_sentences_in_passage, passage_sentence_scores, cleaned_question)
	sentence_number = numpy.argmax(question_scores)

	for option in options:
		cleaned_option = CleanSentence(option, addSynonyms = True)
		option_scores = SentenceSimilarities(cleaned_sentences_in_passage, passage_sentence_scores, cleaned_option, weighted = sentence_number)
		choice_probabilities.append(max(option_scores))

	total_choice_probabilities = sum(choice_probabilities)
	choice_probabilities = [probability / total_choice_probabilities for probability in choice_probabilities]

	answers.append(choice_probabilities)

	return answers

