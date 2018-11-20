# /app/admin/views.py


# Import flask dependencies
from flask import request, render_template, \
      				session, redirect, url_for, Response, jsonify

from . import admin

from app.models import Student, Teacher

from sqlalchemy import func, distinct

from .. import db

headers = "application/json"

@admin.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
	print("Displaying Admin Dashboard")
	student_count = db.session.query(func.count(Student.usn)).first()
	teacher_count = db.session.query(func.count(Teacher.f_id)).first()
	# course_count = db.session.query(func.count(CourseBase.course_name))
	teacher_names = db.session.query(Teacher.name).all()
	sections = db.session.query(distinct(Student.section)).all()
	# course_names = session.query(func.count(distinct(CourseBase.course_name)))

	teacher_list = []
	for obj in teacher_names:
		# print(type(obj))
		teacher_list.append(obj[0])
		teacher_list.sort()

	section_list = []
	for obj in sections:
		# print(type(obj))
		section_list.append(obj[0])
		section_list.sort()

	response = {"student_count" : student_count[0], "teacher_count" : teacher_count[0], "teacher_names" : teacher_list, "sections" : section_list}

	# return str(response)
	return render_template('admin.html', response = response)
							#  ,
							# 			course_names = course_names,
							# 			course_count = course_count,				
							# )


@admin.route('/courses', methods = ['GET', 'POST'])
def courses():
	print("Displaying Courses Page for the Admin")
	return render_template('courselist.html')

@admin.route('/students', methods = ['GET', 'POST'])
def students():
	print("Displaying Students Page for the Admin")
	student_info = db.session.query(Student).filter(Student.role == 'Student').all()
	print(student_info)
	return render_template('studentlist.html')

@admin.route('/teachers', methods = ['GET', 'POST'])
def teachers():
	print("Displaying Teachers Page for the Admin")
	return render_template('teacherlist.html')