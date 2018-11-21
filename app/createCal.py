#!/usr/bin/env python
#import sys 
from pprint import pprint
from oauth2client import client
from googleapiclient import sample_tools
import datetime, sys
from datetime import timedelta

# sample_tools is where they tucked away all the magic and swept it all under the rug
# https://github.com/google/google-api-python-client/blob/master/googleapiclient/sample_tools.py
#
# name of the api: find a list of apis and links to reference here:
# https://developers.google.com/api-client-library/python/apis/
#
# pydoc:
# https://developers.google.com/resources/api-libraries/documentation/calendar/v3/python/latest/

calendarId = None 
service = None
flags = None
summary = None 
startTime = None
endTime = None

def createCalendar():
	global calendarId
	try:
		calendar = {
			'summary': 'This is a test calendar',
			'timeZone': 'Asia/Kolkata'
		}
		created_calendar = service.calendars().insert(body=calendar).execute()
		print(created_calendar['id'])
		calendarId = created_calendar['id']

	except client.AccessTokenRefreshError:
		print('The credentials have been revoked or expired, please re-run the application to re-authorize.')
	
	return calendarId

def getEvents():
	global calendarId
	calendar_list_entry = service.calendarList().get(calendarId=calendarId).execute()
	print(calendar_list_entry['summary'])
	page_token = None
	while True:
		events = service.events().list(calendarId=calendarId, pageToken=page_token).execute()
		for event in events['items']:
			print(event['summary'])
		page_token = events.get('nextPageToken')
		if not page_token:
			break
	return events
	
def addEvent():
	global summary
	global startTime
	global endTime
	global service
	global flags

	if(summary is None):
		summary = 'default'
	if(startTime is None):
		a = str(datetime.datetime.now()).split(".")[0]
		b = a.split(" ")
		c = b[0] + 'T' + b[1]
		startTime = c + '+05:30'
	if(endTime is None):
		a = str(datetime.datetime.now()+timedelta(hours=5) ).split(".")[0]
		b = a.split(" ")
		c = b[0] + 'T' + b[1]
		endTime = c + '+05:30'
	event = {
	'summary': summary,
	'location': 'PES University',
	'description': 'A chance to hear more about Google\'s developer products.',
	'start': {
		'dateTime': startTime,
		'timeZone': 'Asia/Kolkata',
	},
	'end': {
		'dateTime': endTime,
		'timeZone': 'Asia/Kolkata',
	},
	}

	event = service.events().insert(calendarId=calendarId, body=event).execute()
	print ('Event created: %s' % (event.get('htmlLink')))
	return event
	
def constructService(argv):
	global service
	global flags
	# Authenticate and construct service.
	service, flags = sample_tools.init(
		argv, 'calendar', 'v3', 
		__doc__, __file__,
		scope='https://www.googleapis.com/auth/calendar')
	#return service, flags

def setVariables():
	global summary
	global startTime
	global endTime
	summary=None
	startTime=None
	endTime=None
	#return summary,startTime,endTime

def start(argv):
	constructService(argv)
	setVariables()
	'''calendarId = createCalendar()
	addEvent()
	getCalendar()'''
	

#start(argv)

