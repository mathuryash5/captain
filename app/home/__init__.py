# /app/course/__init__.py
from flask import Blueprint

home = Blueprint('home', __name__, url_prefix='', template_folder='../templates/home')

from . import views
 
