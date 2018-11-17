from app import db
from app.models import User, Student, Teacher  


def student_data():
	"""Seeds the Student Table."""
	db.session.add(Student(usn="001", name="abc", email="abc@abc.com", branch="CSE", semester=7, section="A"))
	db.session.add(Student(usn="002", name="def", email="def@def.com", branch="CSE", semester=7, section="B"))
	db.session.add(Student(usn="003", name="xyz", email="xyz@xyz.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn="310", name="Srishti", email="srishtimishra56@gmail.com", branch="CSE", semester=7, section="F"))
	db.session.commit()

def teacher_data():
	"""Seeds the Teacher Table."""
	db.session.add(Teacher(f_id="001", name="Priya", email="priya@abc.com", branch="CSE", position="Professor"))
	db.session.add(Teacher(f_id="002", name="Teacher1", email="teacher1@abc.com", branch="CSE", position="Assistant Professor"))
	db.session.add(Teacher(f_id="003", name="Teacher2", email="teacher2@abc.com", branch="ECE", position="Assistant Professor"))
	db.session.add(Teacher(f_id="004", name="Teacher3", email="teacher3@abc.com", branch="EEE", position="Professor"))
	db.session.commit()

def course_data():
	"""Seeds the Course Table."""

