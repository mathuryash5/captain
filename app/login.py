from requests_oauthlib import OAuth2Session

from app import login_manager
from app.models import User, Student, Teacher, Admin


from . import db


# Google Auth API details
class Auth:
	CLIENT_ID = ('630861931474-mqa933274lsoctu9r94rb0j4tas2o6r6.apps.googleusercontent.com')
	CLIENT_SECRET = 'gUOr5-q89miUNIwEtTciEC2f'
	REDIRECT_URI = 'https://localhost:5000/gCallback'
	AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
	TOKEN_URI = 'https://www.googleapis.com/oauth2/v3/token'
	USER_INFO = 'https://www.googleapis.com/plus/v1/people/me/openIdConnect'
	# USER_INFO = 'https://www.googleapis.com/oauth2/v3/userinfo?alt=json'
	SCOPE = ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
	#USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'



'''
	Creates OAuth session object, used by login functions below
'''
@login_manager.user_loader
def load_user(email):
	print(email)
	a = db.session.query(Admin).filter(Admin.email==email).first()
	if a:
		return a
	u, isTeacher = checkUser(email)
	return u

def get_google_auth(state=None, token=None):
	if token:
		return OAuth2Session(Auth.CLIENT_ID, token=token)
	if state:
		return OAuth2Session(
			Auth.CLIENT_ID,
			state=state,
			redirect_uri=Auth.REDIRECT_URI)
	oauth = OAuth2Session(
		Auth.CLIENT_ID,
		redirect_uri=Auth.REDIRECT_URI,
		scope=Auth.SCOPE)
	return oauth

def checkUser(userEmail):
	try:
		print("Are you a teacher?")
		user = db.session.query(Teacher).filter(Teacher.email==userEmail).first()
		print(user)
		if user:
			print("Is a teacher")
			return user, 1
		else:
			print("Student Check?")
			try:
				print("Are you a student?")
				user = db.session.query(Student).filter(Student.email==userEmail).first()
				if user:
					print("Is a student")
					return user, 0
			except:
				print("Error querying student information")
	except:
		print("Error querying teacher information")


	return -1
 
