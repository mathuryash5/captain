import requests
from flask import Flask, jsonify
import json
app = Flask(__name__)
@app.route("/")

@app.route("/", methods=['GET'])
def main():
	user = 'mathuryash5'
	repo = 'captain'
	return json.dumps(get_stat(user,repo))



def get_stat(user, repo):
	request = 'https://api.github.com/repos/'+user+'/'+repo
	a = requests.get(request+'/stats/contributors').content
	b = requests.get(request+'/contributors').content
	return parseJSON(a,b)


def parseJSON(a,b):
	stats = json.loads(a)
	cont = json.loads(b)
	final_stats = {}
	final_cont = {}
	for i in range(len(cont)):
		temp = cont[i]["login"]
		final_cont[temp] = cont[i]["contributions"]
	for i in range(len(stats)):
		temp = stats[i]["total"]
		login = stats[i]["author"]["login"]
		final_stats[login] = temp
	final = {}
	final["contributions"]=final_cont
	final["commits"]=final_stats
	return final
	
if __name__ == '__main__':
    app.run(debug=True)