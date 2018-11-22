# /app/student/views.py


# Import flask dependencies
from flask import request, render_template, make_response, \
					session, redirect, url_for, Response, jsonify

from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin

from . import student

from app.models import Student, Teacher, CourseBase, CourseResource, CourseDeliverable

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

@student.route('/course/<subject_name>', methods = ['GET', 'POST'])
@login_required
def course(subject_name):
	user_info = db.session.query(Student).filter(Student.email == current_user.email).first()
	course_info = db.session.query(CourseBase.description).filter(CourseBase.course_name == subject_name).first()
	course_names = db.session.query(CourseBase.course_name).filter(CourseBase.semester == user_info.semester).all()
	course_code = db.session.query(CourseBase.course_code).filter(CourseBase.course_name == subject_name).first()
	resources = db.session.query(CourseResource).filter(CourseResource.course_code == course_code[0]).all()
	deliverables = db.session.query(CourseDeliverable).filter(CourseDeliverable.course_code == course_code[0]).all()
	print("="*30)
	print(user_info)
	print(user_info.semester)
	print(user_info.lab_marks)
	print(course_info)
	print("Resources", resources)
	print("="*30)

	response = {"student_name" : user_info.name, "lab_marks" : user_info.lab_marks, "course_info" : course_info[0], 
				"course_names" : course_names, "current_course" : subject_name,
				"resources" : resources, "deliverables" : deliverables}
	return render_template("course.html", response = response)

@student.route('/classmembers/<subject_name>', methods = ['GET', 'POST'])
@login_required
def classmembers(subject_name):
	print("Displaying classmembers")
	user_info = db.session.query(Student).filter(Student.email == current_user.email).first()
	course_info = db.session.query(CourseBase).filter(CourseBase.semester == user_info.semester)
	class_mates = db.session.query(Student).filter(Student.semester == user_info.semester and Student.section == user_info.section).all()
	course_names = db.session.query(CourseBase.course_name).filter(CourseBase.semester == user_info.semester).all()	
	#Filter students out who already have a team.
	# print(Student.has_team[subject_name])
	# available_students = db.session.query(Student).filter(Student.has_team[subject_name].astext.cast(Unicode) == str(0)).all()

	print("="*30)

	print(user_info)
	print(user_info.semester)
	print(user_info.lab_marks)
	# print(available_students)
	print(course_info)
	print("="*30)
	response = {"student_name" : user_info.name, "lab_marks" : user_info.lab_marks, "course_info" : course_info, "class_mates" : class_mates
				, "course_names" : course_names, "subject_name" : subject_name}
	return render_template('classmembers.html', response = response)

@student.route('/create_team/<course_name>', methods = ['POST'])
@login_required
def create_team(course_name):
	print("Adding the team")
	data = request.get_json(force = True)
	usn_list = data['teamUSN']
	course_code = db.session.query(CourseBase.course_code).filter(CourseBase.course_name == course_name)
	session_count = db.session.query(func.count(Team.session_id)).first()
	db.session.add(Team(course_code = course_code[0], session_id = session_count[0], usn_list = {"member_1" : usn_list[0], "member_2" : usn_list[1], "member_3" : usn_list[2]}))
	db.session.commit()
	print("Done adding")
	return jsonify({"status":200})

 
