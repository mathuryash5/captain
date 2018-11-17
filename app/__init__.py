# /app/__init__.py

from flask import Flask, render_template

from flask_mail import Mail
from flask_migrate import Migrate
from flask_login import LoginManager 
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy 

from config import Config


mail = Mail()
db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)	
	bootstrap.init_app(app)
	mail.init_app(app)
	db.init_app(app)
	migrate.init_app(app, db)
	# attach routes and custom error pages here
	from app.student import student as student_blueprint
	from app.teacher import teacher as teacher_blueprint
	from app.admin import admin as admin_blueprint
	app.register_blueprint(student_blueprint)
	app.register_blueprint(teacher_blueprint)
	app.register_blueprint(admin_blueprint)
	@app.shell_context_processor
	def ctx():
		return {'app': app, 'db': db}
	
	return app
