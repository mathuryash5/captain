 # /app/teacher/views.py


# Import flask dependencies
from flask import request, render_template, \
					session, redirect, url_for, Response, jsonify

from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin

from . import teacher

from app.models import Student, Teacher, CourseBase

from sqlalchemy import func, distinct
import json, requests

from .. import db

# Import login related functionality
from app.login import get_google_auth, checkUser, load_user

headers = "application/json" 


# helper functions for gitstats
def get_stat(user, repo):
	request = 'https://api.github.com/repos/'+user+'/'+repo
	a = requests.get(request+'/stats/contributors').content
	b = requests.get(request+'/contributors').content
	return parseJSON(a,b)


def parseJSON(a,b):
	stats = json.loads(a)
	cont = json.loads(b)
	final_stats = {}
	final_cont = {}
	for i in range(len(cont)):
		temp = cont[i]["login"]
		final_cont[temp] = cont[i]["contributions"]
	for i in range(len(stats)):
		temp = stats[i]["total"]
		login = stats[i]["author"]["login"]
		final_stats[login] = temp
	final = {}
	final["contributions"]=final_cont
	final["commits"]=final_stats
	return final

@teacher.route('/dashboard', methods = ['GET', 'POST'])
@login_required
def dashboard():
	print("Displaying the Teacher dashboard")
	user_info = db.session.query(Teacher).filter(Teacher.email == current_user.email).first()
	print(user_info)
	courses_taken = user_info.course_to_section.keys()
	print("="*30)
	print(user_info)
	print(user_info.semester)
	print(user_info.lab_marks)
	# print(course_names)
	# print(all_course_names)
	print("="*30)
	response = {"teacher_name" : user_info.name, "courses_taken" : courses_taken, "course_to_section" : user_info.course_to_section}
	return render_template("Teacher.html", response = response)

@teacher.route('/course', methods = ['GET', 'POST'])
@login_required
def course():
	return render_template("course_min.html")

@teacher.route('/submission', methods = ['GET', 'POST'])
@login_required
def submission():
	return render_template("submission_min.html")

@teacher.route('/plagiarism', methods = ['GET', 'POST'])
@login_required
def plagiarism():
	return render_template("plagiarism.html")

@teacher.route('/evaluate', methods = ['GET', 'POST'])
@login_required
def evaluate():
	print("Displaying the Teacher evaluation page")
	user_info = db.session.query(Teacher).filter(Teacher.email == current_user.email).first()
	courses_taken = user_info.course_to_section.keys()

	# Get all users regiestered for their course
	sections_taught = user_info.course_to_section.values()
	print(sections_taught)
	print(courses_taken)
	students_taught = []
	student_to_subject = {}
	for course_name in courses_taken:
		semester_taught = db.session.query(CourseBase.semester).filter(CourseBase.course_name == course_name).first()
		print(semester_taught)
		temp_student = db.session.query(Student).filter(Student.semester == semester_taught[0] and Student.section in sections_taught).all()
		students_taught += temp_student
		for student in temp_student:
			student_to_subject[student.name] = course_name
	print("="*30)
	print(user_info)
	# print(user_info.semester)
	print(students_taught[0].name)
	# print(course_names)
	# print(all_course_names)
	print("="*30)
	response = {"teacher_name" : user_info.name, "courses_taken" : courses_taken, "course_to_section" : user_info.course_to_section, "students_taught" : students_taught, "student_to_course" : student_to_subject}
	return render_template("marks.html", response = response)

@teacher.route('/gitstats', methods = ['GET', 'POST'])
def stats():
	# replace with db calls
	user = 'mathuryash5'
	repo = 'captain'
	response = get_stat(user,repo)
	response['repo_name'] = repo
	print(response, "\n\n")
	return render_template("gitstats.html", response = response)

@teacher.route('/deadline', methods = ['GET', 'POST'])
def deadline():
	# replace with db calls
	return render_template("new_deadline.html")



