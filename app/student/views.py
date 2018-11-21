# /app/student/views.py


# Import flask dependencies
from flask import request, render_template, make_response, \
					session, redirect, url_for, Response, jsonify

from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin

from . import student

from app.models import Student, Teacher, CourseBase, Course

from sqlalchemy import func, distinct

from .. import db
import random
# Import login related functionality
from app.login import get_google_auth, checkUser, load_user

headers = "application/json" 

@student.route('/dashboard', methods = ['GET', 'POST'])
@login_required
def dashboard():
	print("Displaying the Student dashboard")
	user_info = db.session.query(Student).filter(Student.email == current_user.email).first()
	course_names = db.session.query(CourseBase.course_name).filter(CourseBase.semester == user_info.semester).all()
	all_course_names = db.session.query(CourseBase.course_name).all()
	print("="*30)
	print(user_info)
	print(user_info.semester)
	print(user_info.lab_marks)
	print(course_names)
	# print(all_course_names)
	print("="*30)
	response = {"student_name" : user_info.name, "lab_marks" : user_info.lab_marks, "course_names" : course_names}
	return render_template("dashboard.html", response = response)

@student.route('/course', methods = ['GET', 'POST'])
@login_required
def course():
	user_info = db.session.query(Student).filter(Student.email == current_user.email).first()
	course_info = db.session.query(CourseBase).filter(CourseBase.semester == user_info.semester)
	print("="*30)
	print(user_info)
	print(user_info.semester)
	print(user_info.lab_marks)
	print(course_info)
	print("="*30)
	results = {"student_name" : user_info.name, "lab_marks" : user_info.lab_marks, "course_info" : course_info}

	#Set cookies for team info
	teamID = random.randint(1,2)
	response = make_response(render_template("course.html", response = results))
	response.set_cookie('tid', str(teamID), max_age=60*5)
	response.set_cookie('usn', str(current_user.email), max_age=60*5)
	return response

@student.route('/classmembers', methods = ['GET', 'POST'])
@login_required
def classmembers():
	user_info = db.session.query(Student).filter(Student.email == current_user.email).first()
	course_info = db.session.query(CourseBase).filter(CourseBase.semester == user_info.semester)
	class_mates = db.session.query(Student).filter(Student.semester == user_info.semester).all()
	print("="*30)
	print(user_info)
	print(user_info.semester)
	print(user_info.lab_marks)
	print(course_info)
	print("="*30)
	response = {"student_name" : user_info.name, "lab_marks" : user_info.lab_marks, "course_info" : course_info, "class_mates" : class_mates}
	return render_template('classmembers.html', response = response)

 
