 # /app/teacher/views.py


# Import flask dependencies
from flask import request, render_template, \
					session, redirect, url_for, Response, jsonify

from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin

from . import teacher

from app.models import Student, Teacher, CourseBase, Course

from sqlalchemy import func, distinct

from .. import db

# Import login related functionality
from app.login import get_google_auth, checkUser, load_user

headers = "application/json" 

@teacher.route('/dashboard', methods = ['GET', 'POST'])
@login_required
def dashboard():
	print("Displaying the Teacher dashboard")
	user_info = db.session.query(Teacher).filter(Teacher.email == current_user.email).first()
	courses_taken = user_info.course_to_section.keys()
	
	print("="*30)
	print(user_info)
	print(user_info.semester)
	print(user_info.lab_marks)
	print(course_names)
	# print(all_course_names)
	print("="*30)
	response = {"teacher_name" : user_info.name, "courses_taken" : courses_taken, "course_to_section" : user_info.course_to_section}
	return render_template("Teacher.html", response = response)

