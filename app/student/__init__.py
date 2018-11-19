# /app/student/__init__.py
from flask import Blueprint

student = Blueprint('student', __name__, url_prefix='/student', template_folder='../templates/student')

from . import views
 
