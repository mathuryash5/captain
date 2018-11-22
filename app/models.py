# services/users/project/api/models.py

## To-do
## Add marks to the student table(mapping marks to courses?)
## Check if a student has a team.
## Calendar ID with the course ID 
## How do we store the invites sent to a team mate?
## Have timestamp associated with project eval to store the feedback from the teacher.
import datetime

from sqlalchemy.sql import func
from sqlalchemy.schema import PrimaryKeyConstraint
from sqlalchemy.ext.declarative import AbstractConcreteBase


from flask_login import UserMixin

# from app import login_manager
from app import db

class User(db.Model, UserMixin, AbstractConcreteBase):
	__tablename__ = "users"

	# __abstract__ = True

	# college_id = db.Column(db.String(128), primary_key=True)
	name = db.Column(db.String(128), nullable=False)
	email = db.Column(db.String(128), nullable=False, unique = True)
	branch = db.Column(db.String(128))
	role = db.Column(db.String(128))
	active = db.Column(db.Boolean(), default=True, nullable=False)


	def get_id(self):
		"""Return the email address to satisfy Flask-Login's requirements."""
		return self.email

class Admin(User):
	__tablename__ = "admin"

	roleno = db.Column(db.String(128), primary_key = True)
	password = db.Column(db.String(128), nullable=False)

	__mapper_args__ = {
		'polymorphic_identity': 'admin',
	}

	def __init__(self, roleno, password):
		self.roleno = roleno
		self.name = "admin"
		self.email = "admin@captain.edu"
		self.branch = "NA"
		self.role = "Admin"
		self.active = True
		self.password = password

	def __repr__(self):
		return '<AdminProfile {}>'.format(self.email)

class Student(User):
	__tablename__ = "student"

	usn = db.Column(db.String(128), primary_key = True )
	semester = db.Column(db.Integer)
	section = db.Column(db.String(2), nullable = False)
	# A key value pair where the key would the course id and the value denotes team_id
	has_team = db.Column(db.JSON) 
	lab_marks = db.Column(db.JSON)

	__mapper_args__ = {
		'polymorphic_identity': 'student',
	}

	def __init__(self, usn, name, email, branch, semester, section):
		self.usn = usn
		self.name = name
		self.email = email
		self.branch = branch
		self.semester = semester
		self.section = section 
		self.role = "Student"

		def get_course_names(semester):
			course_names = db.session.query(CourseBase.course_name).filter(CourseBase.semester == semester).all()
			return course_names
		lab_marks = {}
		has_team = {}
		for course in get_course_names(semester):
			lab_marks[str(course[0])] = 0
			has_team[str(course[0])] = 0

		self.lab_marks = lab_marks
		self.has_team = has_team

	def __repr__(self):
		return '<UserProfile {}>'.format(self.email)


class Teacher(User):
	__tablename__ = "teacher"
	
	f_id = db.Column(db.String(128), primary_key = True)
	position = db.Column(db.String(128))
	course_to_section = db.Column(db.JSON)

	__mapper_args__ = {
		'polymorphic_identity': 'teacher',
	}

	def __init__(self, f_id, name, email, branch, position, course_to_section):
		self.f_id = f_id
		self.name = name
		self.email = email
		self.branch = branch
		self.position = position
		self.course_to_section = course_to_section
		self.role = "Teacher"

	def __repr__(self):
		return '<TeacherProfile {}>'.format(self.email)


class CourseBase(db.Model):
	__tablename__ = "course_base"

	course_code = db.Column(db.String, unique = True, primary_key =  True)
	course_name = db.Column(db.String)
	description = db.Column(db.Text, nullable = False)
	semester = db.Column(db.Integer)
	branch = db.Column(db.String(128))
	# The constraint on the max number of team members.
	no_of_max_members = db.Column(db.Integer)
	calendar_id = db.Column(db.String(128))
	# teams = db.relationship('Team', backref = 'course', lazy = True)

	def __init__(self, course_name, course_code, description, semester, branch, no_of_max_members, calendar_id):
		self.course_name = course_name
		self.course_code = course_code
		self.description = description
		self.semester = semester
		self.branch = branch
		self.no_of_max_members = no_of_max_members
		## Add the calendar initialization code here
		self.calendar_id = calendar_id

	def __repr__(self):
		return '<CourseBase {}>'.format(self.course_name)



class CourseDeliverable(db.Model):
	__tablename__ = "course_deliverable"

	course_code = db.Column(db.String, db.ForeignKey('course_base.course_code'))
	global_deliverable_id = db.Column(db.Integer, unique = True, autoincrement = True) 
	deliverable_id = db.Column(db.Integer, nullable = False)
	deliverable = db.Column(db.String(256))
	deliverable_deadline = db.Column(db.DateTime(timezone = True))

	def __init__(self, course_code, deliverable, deliverable_deadline):
		self.course_code = course_code
		self.deliverable = deliverable
		self.deliverable_deadline = deliverable_deadline

		def get_deliverables_count():
			# print(course_code)
			deliverables_count = db.session.query(CourseDeliverable).filter(CourseDeliverable.course_code == course_code).count()
			# print(deliverables_count)
			return deliverables_count


		self.deliverable_id = get_deliverables_count() + 1

	def __repr__(self):
		return '<Course {}>'.format(self.course_name)

	__table_args__ = (PrimaryKeyConstraint(course_code, global_deliverable_id),)

class CourseResource(db.Model):
	__tablename__ = "course_resource"

	course_code = db.Column(db.String, db.ForeignKey('course_base.course_code'))
	# Resources supplied by the teacher for the students. 
	resource_desc = db.Column(db.String(256))
	resource_url = db.Column(db.String(256))
	upload_time = db.Column(db.DateTime(timezone = True), default=datetime.datetime.utcnow)

	def __init__(self, course_code, resource_desc, resource_url):
		self.course_code = course_code
		self.rsource_desc = resource_desc
		self.resource_url = resource_url

	def __repr__(self):
		return '<CourseResources{}>'.format(self.course_name)

	__table_args__ = (PrimaryKeyConstraint(course_code, resource_url),) 	 

class Team(db.Model):
	__tablename__ = "team"

	global_team_id = db.Column(db.Integer, autoincrement = True, unique = True)
	team_id = db.Column(db.Integer, nullable = False)
	course_code = db.Column(db.String, db.ForeignKey('course_base.course_code'))
	# IDs required for chat sessions.
	session_id = db.Column(db.Integer, nullable = False, autoincrement =  True)
	usn_list = db.Column(db.JSON)
	github_user = db.Column(db.String(64))
	github_repo = db.Column(db.String(128))
	marks = db.Column(db.Integer)

	def __init__(self, course_code, session_id, usn_list, github_user, github_repo):
		self.course_code = course_code
		self.session_id = session_id
		self.usn_list = usn_list
		self.github_user = github_user
		self.github_repo = github_repo
		def get_team_count():
			team_count = db.session.query(Team).filter(Team.course_code == course_code).count()
			return team_count

		self.team_id = get_team_count() + 1 

	__table_args__ = (PrimaryKeyConstraint(global_team_id, course_code),) 
	

class TeamSubmission(db.Model):
	__tablename__ = "team_submission"

	global_team_id = db.Column(db.Integer, db.ForeignKey('team.global_team_id'))
	course_code = db.Column(db.String, db.ForeignKey('course_base.course_code'))
	global_deliverable_id = db.Column(db.Integer, db.ForeignKey('course_deliverable.global_deliverable_id'))
	resource_url = db.Column(db.String(128))
	grading_status = db.Column(db.Boolean, default = False)
	submission_time = db.Column(db.DateTime(timezone = True), default=datetime.datetime.utcnow)
	teacher_eval = db.Column(db.String(256))
	teacher_eval_time = db.Column(db.DateTime())

	def __init__(self, global_team_id, course_code, global_deliverable_id, resource_url, grading_status, submission_time):
		self.global_team_id = global_team_id
		self.course_code = course_code
		self.global_deliverable_id = deliverable_id
		self.resource_url = resource_url

	__table_args__ = (PrimaryKeyConstraint(global_team_id, course_code, global_deliverable_id),) 