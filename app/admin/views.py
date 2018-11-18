# /app/admin/views.py

# Import flask dependencies
from flask import request, render_template, \
      				session, redirect, url_for

from . import admin

from app.models import Student, Teacher

from sqlalchemy import func, distinct

from .. import db


@admin.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
	print("Displaying Admin Dashboard")
	student_count = db.session.query(func.count(Student.usn))
	teacher_count = db.session.query(func.count(Teacher.f_id))
	# course_count = db.session.query(func.count(CourseBase.course_name))
	teacher_names = db.session.query(Teacher.name)
	sections = db.session.query(func.count(distinct(Student.section)))
	# course_names = session.query(func.count(distinct(CourseBase.course_name)))
	print(student_count, "Registered Students")
	print(teacher_count, "Teachers")
	# print(course_count, "Number of Courses")
	print("Names of teachers", teacher_names)

	return render_template('admin.html',student_count = student_count, 
										teacher_count = teacher_count,
										teacher_names = teacher_names,
										sections = sections
							)
							#  ,
							# 			course_names = course_names,
							# 			course_count = course_count,				
							# )
