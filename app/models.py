# services/users/project/api/models.py

## To-do
## Add marks to the student table(mapping marks to courses?)
## Check if a student has a team.
## Calendar ID with the course ID 
## How do we store the invites sent to a team mate?
## Have timestamp associated with project eval to store the feedback from the teacher.

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
		self.active = True 
		self.role = "Student"

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

	def __init__(self, f_id, name, email, branch, position):
		self.f_id = f_id
		self.name = name
		self.email = email
		self.branch = branch
		self.position = position
		self.active = True
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


class Course(db.Model):
	__tablename__ = "course"

	course_code = db.Column(db.String, db.ForeignKey('course_base.course_code'))
	deliverable_id = db.Column(db.Integer, nullable = False, unique = True)
	deliverables = db.Column(db.String(256))
	deliverable_deadline = db.Column(db.DateTime(timezone = True))
	# Resources supplied by the teacher for the students. 
	teacher_resources = db.Column(db.JSON)

	def __init__(self, course_code, deliverable_id, deliverables, deliverable_deadline, teacher_resources):
		self.course_code = course_code
		self.deliverable_id = deliverable_id
		self.deliverables = deliverables
		self.deliverable_deadline = deliverable_deadline
		self.teacher_resources = teacher_resources

	def __repr__(self):
		return '<Course {}>'.format(self.course_name)

	__table_args__ = (PrimaryKeyConstraint(course_code, deliverable_id),) 

class Team(db.Model):
	__tablename__ = "team"

	# NEED TO FIX THIS!
	team_id = db.Column(db.Integer, nullable = False, unique = True)
	# , autoincrement = True)
	course_code = db.Column(db.String, db.ForeignKey('course_base.course_code'))
	# IDs required for chat sessions.
	session_id = db.Column(db.Integer, nullable = False, autoincrement =  True)
	usn_list = db.Column(db.JSON)
	github_user = db.Column(db.String(64))
	github_repo = db.Column(db.String(128))
	marks = db.Column(db.Integer)

	def __init__(self, team_id, course_code, session_id, usn_list, github_user, github_repo):
		self.team_id = team_id
		self.course_code = course_code
		self.session_id = session_id
		self.usn_list = usn_list
		self.github_user = github_user
		self.github_repo = github_repo

	__table_args__ = (PrimaryKeyConstraint(team_id, course_code),) 
	

class TeamSubmissions(db.Model):
	__tablename__ = "team_submissions"

	team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))
	course_code = db.Column(db.String, db.ForeignKey('course_base.course_code'))
	deliverable_id = db.Column(db.Integer, db.ForeignKey('course.deliverable_id'))
	resource_url = db.Column(db.String(128))
	grading_status = db.Column(db.Boolean, default = True)
	submission_time = db.Column(db.DateTime(timezone = True))

	__table_args__ = (PrimaryKeyConstraint(team_id, course_code, deliverable_id),) 


# # @login_manager.user_loader
# # def load_user(id):
# # 	try: 
# # 		return User.query.get(int(id))
# # 	except:
# # 		return None