from app import db
from app.models import User, Student, Teacher, CourseBase, Course


def student_data():
	"""Seeds the Student Table."""
	db.session.add(Student(usn = "001", name="abc", email="abc@abc.com", branch="CSE", semester=7, section="A"))
	db.session.add(Student(usn = "002", name="def", email="def@def.com", branch="CSE", semester=7, section="B"))
	db.session.add(Student(usn = "003", name="xyz", email="xyz@xyz.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn = "310", name="Srishti", email="srishtimishra56@gmail.com", branch="CSE", semester=7, section="F"))
	db.session.commit()

def teacher_data():
	"""Seeds the Teacher Table."""
	db.session.add(Teacher(f_id = "f001", name="Priya", email="priya@abc.com", branch="CSE", position="Professor"))
	db.session.add(Teacher(f_id = "f002", name="Teacher1", email="teacher1@abc.com", branch="CSE", position="Assistant Professor"))
	db.session.add(Teacher(f_id = "f003", name="Teacher2", email="teacher2@abc.com", branch="ECE", position="Assistant Professor"))
	db.session.add(Teacher(f_id = "f004", name="Teacher3", email="teacher3@abc.com", branch="EEE", position="Professor"))
	db.session.commit()

def coursebase_data():
	"""Seeds the CourseBase Table."""
	db.session.add(CourseBase(course_name = "Unix System Programming", course_code = "UE15CS101", description = "Text1", semester = 6, branch = "CSE", no_of_max_members = 3, calendar_id = "xyz"))
	db.session.add(CourseBase(course_name = "Introduction to Data Science", course_code = "UE15CS201", description = "Text2", semester = 3, branch = "CSE", no_of_max_members = 3, calendar_id = "xyz"))
	db.session.add(CourseBase(course_name = "Operating Systems", course_code = "UE15CS301", description = "Text3", semester = 5, branch = "CSE", no_of_max_members = 3, calendar_id = "xyz"))
	db.session.add(CourseBase(course_name = "Software Engineering", course_code = "UE15CS401", description = "Text4", semester = 7, branch = "CSE", no_of_max_members = 3, calendar_id = "xyz"))
	db.session.commit()

def course_data():
	"""Seeds the Course Table."""
	db.session.add(Course(course_code = "UE15CS101", deliverables = "del1", deliverable_deadline = ""))
	db.session.add(Course(course_code = "UE15CS101", deliverables = "del2", deliverable_deadline = ""))
	db.session.add(Course(course_code = "UE15CS301", deliverables = "del1", deliverable_deadline = ""))
	db.session.add(Course(course_code = "UE15CS401", deliverables = "del1", deliverable_deadline = ""))
	db.session.commit()

def team_data():
	"""Seeds the Team Table."""
	




