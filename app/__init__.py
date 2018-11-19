# /app/__init__.py

from flask import Flask, render_template

from flask_mail import Mail
from flask_migrate import Migrate
from flask_login import LoginManager 
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy 

from config import Config

from OpenSSL import SSL


mail = Mail()
db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
login_manager = LoginManager()

def create_app():
	# SSL support
	context = ('server.crt', 'server.key')

	#Init
	app = Flask(__name__)
	app.config.from_object(Config)	
	bootstrap.init_app(app)
	mail.init_app(app)
	db.init_app(app)
	migrate.init_app(app, db)

	# Init login
	app.secret_key = 'somethingsecret'
	login_manager.login_view = "home.login"
	login_manager.session_protection = "strong"
	login_manager.init_app(app)

	# attach routes and custom error pages here
	from app.student import student as student_blueprint
	from app.teacher import teacher as teacher_blueprint
	from app.admin import admin as admin_blueprint
	from app.home import home as home_blueprint
	app.register_blueprint(student_blueprint)
	app.register_blueprint(teacher_blueprint)
	app.register_blueprint(admin_blueprint)
	app.register_blueprint(home_blueprint)
	@app.shell_context_processor
	def ctx():
		return {'app': app, 'db': db}
	
	return app
