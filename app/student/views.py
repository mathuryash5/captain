# /app/student/views.py


# Import flask dependencies
from flask import request, render_template, \
      				session, redirect, url_for, Response, jsonify

from . import student

from app.models import Student, Teacher

from sqlalchemy import func, distinct

from .. import db

headers = "application/json" 

@student.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
	return render_template('dashboard.html')

@student.route('/course', methods = ['GET', 'POST'])
def course():
	return render_template('course.html')

@student.route('/classmembers', methods = ['GET', 'POST'])
def classmembers():
	return render_template('classmembers.html')

