# /app/student/views.py


# Import flask dependencies
from flask import request, render_template, \
      				session, redirect, url_for, Response, jsonify

from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin

from . import student

from app.models import Student, Teacher

from sqlalchemy import func, distinct

from .. import db

# Import login related functionality
from app.login import get_google_auth, checkUser, load_user

headers = "application/json" 

@student.route('/dashboard', methods = ['GET', 'POST'])
@login_required
def dashboard():
	print("Displaying the Student dashboard")
	current_user = load_user(current_user.email)
	response = {"student_name" : current_user.name}
	print(response)
	return render_template('dashboard.html', response = response)

@student.route('/course', methods = ['GET', 'POST'])
@login_required
def course():
	return render_template('course.html')

@student.route('/classmembers', methods = ['GET', 'POST'])
@login_required
def classmembers():
	return render_template('classmembers.html')

 
