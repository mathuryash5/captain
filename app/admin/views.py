# /app/admin/views.py


# Import flask dependencies
from flask import request, render_template, \
      				session, redirect, url_for, Response, jsonify

from flask_login import LoginManager, login_required, login_user, logout_user, current_user


from . import admin

from app.models import Student, Teacher, Admin, CourseBase

from sqlalchemy import func, distinct

from .. import db, home

headers = "application/json"

'''
	This function
		renders admin dashboard
'''

@admin.route('/dashboard', methods = ['GET', 'POST'])
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

'''
	This function
		renders dashboard to manage courses
'''

@admin.route('/courses', methods = ['GET', 'POST'])
def courses():
	print("Displaying Courses Page for the Admin")
	return render_template('courselist.html')

'''
	This function
		renders dashboard to manage students
'''

@admin.route('/students', methods = ['GET', 'POST'])
def students():
	print("Displaying Students Page for the Admin")
	student_info = db.session.query(Student).filter(Student.role == 'Student').all()
	print(student_info)
	return render_template('studentlist.html', response = student_info)

'''
	This function
		renders dashboard to manage teachers
'''
@admin.route('/teachers', methods = ['GET', 'POST'])
def teachers():
	print("Displaying Teachers Page for the Admin")
	teacher_info = db.session.query(Teacher).filter(Teacher.role == 'Teacher').all()
	print(teacher_info)
	return render_template('teacherlist.html', response = teacher_info)

'''
	This function
		renders login page
'''
@admin.route('/login', methods=['GET'])
def login():
	return render_template('adminlogin.html')


@admin.route('/verify', methods=['POST'])
def verify():
	print("Verifying", request.form['admin-email'])
	print(db.session.query(Admin).filter(Admin.email == "admin@captain.edu").first())
	user_data = db.session.query(Admin).filter(Admin.email == request.form['admin-email']).first()
	if user_data:
		if request.form['admin-pwd'] == user_data.password:
			current_user.name = user_data.name
			current_user.email = user_data.email
			return dashboard()
		else:
			return jsonify({"status": "fail", "msg":"wrong password"})
	else:
		return jsonify({"status": "fail", "msg":"invalid credentials"})


@admin.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    # db.session.add(user)
    # db.session.commit()
    logout_user()
    return redirect(url_for(home))