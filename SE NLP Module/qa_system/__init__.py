import os
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager
from flask_mail import Mail 
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e9def8c3066b8241217176a15038a6c0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
UPLOAD_FOLDER = 'qa_system/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)

mail = Mail(app)

from qa_system import routes

app.run(port = "1234")
