# services/users/project/api/models.py

## To-do
## Add marks to the student table(mapping marks to courses?)
## Check if a student has a team.
## Calendar ID with the course ID 
## How do we store the invites sent to a team mate?


from sqlalchemy.sql import func

from flask_login import UserMixin

# from app import login_manager
from app import db

class User(db.Model, UserMixin):
	__tablename__ = "users"

	id = db.Column(db.String(128), primary_key=True)
	name = db.Column(db.String(128), nullable=False)
	email = db.Column(db.String(128), nullable=False, unique = True)
	branch = db.Column(db.String(128))
	role = db.Column(db.String(128))



class Student(User):
	__tablename__ = "student"

	usn = db.Column(db.String(128), db.ForeignKey('users.id'), primary_key = True )
	semester = db.Column(db.Integer)
	section = db.Column(db.String(2))
	# A key value pair where the key would the course id and the value denotes team_id
	has_team = db.Column(db.JSON) 
	marks = db.Column(db.JSON)

	def __init__(self, usn, name, email, branch, semester, section):
		self.usn = usn
		self.name = name
		self.email = email
		self.branch = branch
		self.semester = semester
		self.section = section 
		self.role = "Student"

	def __repr__(self):
		return '<UserProfile {}>'.format(self.name)

class Teacher(User):
	__tablename__ = "teacher"
	
	f_id = db.Column(db.String(128))
	position = db.Column(db.String(128))
	course_to_section = db.Column(db.JSON)

	def __init__(self, f_id, name, email, branch, position):
		self.f_id = f_id
		self.name = name
		self.email = email
		self.branch = branch
		self.position = position
		self.role = "Teacher"

	def __repr__(self):
		return '<TeacherProfile {}>'.format(self.name)

# class CourseBase(db.Model):
# 	__tablename__ = "course_base"

# 	course_name = db.Column(db.String, primary_key = True)
# 	course_id = db.Column(db.Integer, unique = True)
# 	description = db.Column(db.Text, nullable = False)
# 	semester = db.Column(db.Integer)
# 	# The constraint on the max number of team members.
# 	no_of_max_members = db.Column(db.Integer)
# 	calendar_id = db.Column(db.String(128))
# 	teams = db.relationship('Team', backref = 'course', lazy = True)

# 	def __init__(self, course_name, course_id, description, semester, no_of_max_members, calendar_id):
# 		self.course_name = course_name
# 		self.course_id = course_id
# 		self.description = description
# 		self.semester = semester
# 		self.no_of_max_members = no_of_max_members
# 		## Add the calendar initialization code here
# 		self.calendar_id = calendar_id

# 	def __repr__(self):
# 		return '<CourseBase {}>'.format(self.course_name)


# class Course(db.Model):
# 	__tablename__ = "course"

# 	course_id = db.Column(db.Integer, db.ForeignKey('coursebase.course_id'))
# 	deliverable_id = db.Column(db.Integer, nullable = False, primary_key = True)
# 	deliverables = db.Column(db.String(256))
# 	deliverable_deadline = db.Column(db.DateTime(timezone = True))
# 	# Resources supplied by the teacher for the students. 
# 	teacher_resources = db.Column(db.JSON)

# 	def __init__(self, course_id, deliverable_id, deliverables, deliverable_deadline, teacher_resources):
# 		self.course_id = course_id
# 		self.deliverable_id = deliverable_id
# 		self.deliverables = deliverables
# 		self.deliverable_deadline = deliverable_deadline
# 		self.teacher_resources = teacher_resources

# 	def __repr__(self):
# 		return '<Course {}>'.format(self.course_name)


# class Team(db.Model):
# 	__tablename__ = "team"

# 	team_id = db.Column(db.Integer, primary_key = True)
# 	course_id = db.Column(db.Integer, db.ForeignKey('coursebase.course_id'))
# 	# IDs required for chat sessions.
# 	session_id = db.Column(db.Integer, nullable = False)
# 	usn_list = db.Column(db.JSON)
# 	github_user = db.Column(db.String(64))
# 	github_repo = db.Column(db.String(128))

# 	def __init__(self, team_id, course_id, session_id, usn_list, github_user, github_repo):
# 		self.team_id = team_id
# 		self.course_id = course_id
# 		self.session_id = session_id
# 		self.usn_list = usn_list
# 		self.github_user = github_user
# 		self.github_repo = github_repo

# # class TeamSubmissions(db.Model):
# # 	__tablename__ = "team_submissions"

# # 	team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))
# # 	deliverable_id = db.Column(db.Integer)
# # 	resource_url = db.Column(db.String(128))
# # 	grading_status = db.Column(db.Boolean, default = True)
# # 	submission_time = db.Column(db.DateTime(timezone = True))



# # @login_manager.user_loader
# # def load_user(id):
# # 	try:
# # 		return User.query.get(int(id))
# # 	except:
# # 		return None