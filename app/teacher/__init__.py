# /app/teacher/__init__.py
from flask import Blueprint

teacher = Blueprint('teacher', __name__, url_prefix='/teacher', template_folder='../templates/teacher')

from . import views
 
