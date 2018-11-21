import requests
from flask import Flask, jsonify
import json, sys
import createCal 
app = Flask(__name__)
@app.route("/")

@app.route("/createCalendar", methods=['GET'])
def createCalendar():
	createCal.start(sys.argv)
	return createCal.createCalendar()
	

@app.route("/getEvents", methods=['GET'])
def getEvents():
	return json.dumps(createCal.getEvents())
	
@app.route("/addEvent", methods=['GET','POST'])
def addEvent():
	return json.dumps(createCal.addEvent())
	
if __name__ == '__main__':
    app.run(debug=True)