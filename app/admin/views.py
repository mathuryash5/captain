# /app/admin/views.py


# Import flask dependencies
from flask import request, render_template, \
      				session, redirect, url_for, Response, jsonify, flash

from . import admin

from app.models import Student, Teacher, CourseBase

from sqlalchemy import func, distinct

from .. import db, mail

headers = "application/json"

@admin.route('/dashboard', methods = ['GET'])
def dashboard():
	print("Displaying Admin Dashboard")
	student_count = db.session.query(func.count(Student.usn)).first()
	teacher_count = db.session.query(func.count(Teacher.f_id)).first()
	course_count = db.session.query(func.count(CourseBase.course_name)).first()
	teacher_names = db.session.query(Teacher.name).all()
	sections = db.session.query(distinct(Student.section)).all()
	course_names = db.session.query(CourseBase.course_name).all()
	semester = db.session.query(distinct(Student.semester)).all()

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

	semester_count = {}
	for obj in semester:
		student_sem_cnt = db.session.query(Student).filter(Student.semester == obj[0]).count()
		semester_count[str(obj[0])] = student_sem_cnt

	print(semester_count)

	course_list = []
	for obj in course_names:
		course_list.append(obj[0])
	course_list.sort()

	response = {"student_count" : student_count[0], "course_count" : course_count[0], "teacher_count" : teacher_count[0],
				 "teacher_names" : teacher_list, "sections" : section_list, "course_names" : course_list}

	# return str(response)
	return render_template('admin.html', response = response, bar_chart = semester_count)
							#  ,
							# 			course_names = course_names,
							# 			course_count = course_count,				
							# )

@admin.route('/dashboard', methods = ['POST'])
def send_mail():
	print("Sending Users email notification")
	data = request.get_json(force = True)
	users = ["mathuryash5@gmail.com"]
	with mail.connect() as conn:
	    for user in users:
	        message = '...'
	        subject = "hello, %s" % user.name
	        msg = Message(recipients=[user.email],
	                      body=message,
	                      subject=subject)

	        conn.send(msg)

@admin.route('/courses', methods = ['GET', 'POST'])
def courses():
	print("Displaying Courses Page for the Admin")
	return render_template('courselist.html')

@admin.route('/students', methods = ['GET'])
def students():
	print("Displaying Students Page for the Admin")
	student_info = db.session.query(Student).filter(Student.role == 'Student').all()
	print(student_info)
	return render_template('studentlist.html', response = student_info)

@admin.route('/add/<type>', methods = ['POST'])
def add_data(type):
	print("Adding new user")
	data = request.get_json(force = True)	
	print(type(data))
	if(type == "student"):
		exists = db.session.query(Student.usn).filter_by(usn=data['usn']).scalar() is not None
		# If student exists
		if exists:
			flash("User already exists!")
		#add student
		else:
			flash("New User added")
			db.session.add(Student(usn=data['usn'], name=data['name'], email=data['email'], branch=data['branch'], semester=data['semester'], section=data['section']))
			db.session.commit()
		student_info = db.session.query(Student).filter(Student.role == 'Student').all()
		return render_template('studentlist.html', response = student_info)
	elif(type == "teacher"):
		exists = db.session.query(Teacher.f_id).filter_by(f_id=data['f_id']).scalar() is not None
		#If teacher exists
		if exists:
			flash("User already exists!")
		#add teacher
		else:
			flash("New User added")
			db.session.add(Teacher(f_id = data['f_id'], name=data['name'], email=data['email'], branch=data['branch'], position=data['position']))
			db.session.commit()
		teacher_info = db.session.query(Teacher).filter(Teacher.role == 'Teacher').all()
		return render_template('teacherlist.html', response = teacher_info)
	elif(type == "course"):
		exists = db.session.query(CourseBase.course_code).filter_by(course_code=data['course_code']).scalar() is not None
		#If teacher exists
		if exists:
			flash("Course already exists!")
		#add teacher
		else:
			flash("New Course added")
			db.session.add(CourseBase(course_name = data['course_name'], course_code = data['course_code'], description = data['description'], semester = data['semester'], branch = data['branch'], no_of_max_members = data['no_of_max_members'], calendar_id = "xyz"))
			db.session.commit()
		print("Displaying Courses Page for the Admin")
		return render_template('courselist.html')
			

@admin.route('/teachers', methods = ['GET'])
def teachers():
	print("Displaying Teachers Page for the Admin")
	teacher_info = db.session.query(Teacher).filter(Teacher.role == 'Teacher').all()
	print(teacher_info)
	return render_template('teacherlist.html', response = teacher_info)



