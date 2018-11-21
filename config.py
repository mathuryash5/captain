import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'

	CAPTAIN_MAIL_SUBJECT_PREFIX = '[captain]'
	CAPTAIN_MAIL_SENDER = 'Captain Admin <abc@example.com>'
	# CAPTAIN_ADMIN = os.environ.get('CAPTAIN_ADMIN'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or "captain.se6@gmail.com"
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or "helloworld!"

	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/captain' 
	SQLALCHEMY_TRACK_MODIFICATIONS = False #do not send a signal to the application everytime a change is made in db

	@staticmethod
	def init_app(app):
		pass
