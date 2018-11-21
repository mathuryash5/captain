from app import db
from app.models import User, Student, Teacher, CourseBase, Course


def student_data():
	"""Seeds the Student Table."""
	db.session.add(Student(usn = "01FB15ECS001", name="Aditya Ramani", email="aditya.ramani@gmail.com", branch="CSE", semester=7, section="A"))
	db.session.add(Student(usn = "01FB15ECS002", name="Anvith Shetty", email="anvith.shetty@gmail.com", branch="CSE", semester=7, section="A"))
	db.session.add(Student(usn = "01FB15ECS003", name="Saket Golyan", email="saket.golyan@gmail.com", branch="CSE", semester=7, section="A"))
	db.session.add(Student(usn = "01FB15ECS004", name="Advait Jha", email="advait.jha@gmail.com", branch="CSE", semester=5, section="A"))
	db.session.add(Student(usn = "01FB15ECS005", name="Aditya Vir Roy", email="aditya.vir.roy@gmail.com", branch="CSE", semester=5, section="A"))
	db.session.add(Student(usn = "01FB15ECS006", name="Anirudh Gupta", email="anirudh.gupta@gmail.com", branch="CSE", semester=3, section="A"))
	db.session.add(Student(usn = "01FB15ECS007", name="Anubhav Agarwal", email="anubhav.agarwal@gmail.com", branch="CSE", semester=3, section="A"))
	db.session.add(Student(usn = "01FB15ECS008", name="Rohan Agarwal", email="rohan.agarwal@gmail.com", branch="CSE", semester=3, section="A"))
	db.session.add(Student(usn = "01FB15ECS009", name="Zayaan Khodaiji", email="zayaan.khodaiji@gmail.com", branch="CSE", semester=3, section="A"))
	db.session.add(Student(usn = "01FB15ECS010", name="Atharva Matta", email="atharva.matta@gmail.com", branch="CSE", semester=3, section="A"))
	db.session.add(Student(usn = "01FB15ECS011", name="Aditya Gandhi", email="aditya.gandhi@gmail.com", branch="CSE", semester=5, section="B"))
	db.session.add(Student(usn = "01FB15ECS012", name="Mrigank Khemka", email="mrigank.khemka@gmail.com", branch="CSE", semester=5, section="B"))
	db.session.add(Student(usn = "01FB15ECS013", name="Vatsal Agarwal", email="vatsal.agarwal@gmail.com", branch="CSE", semester=5, section="B"))
	db.session.add(Student(usn = "01FB15ECS014", name="Aayushman Arora", email="aayushman.arora@gmail.com", branch="CSE", semester=7, section="B"))
	db.session.add(Student(usn = "01FB15ECS015", name="Rahil Arora", email="rahil.arora@gmail.com", branch="CSE", semester=7, section="B"))
	db.session.add(Student(usn = "01FB15ECS016", name="Armaan Imaam", email="armaan.imaam@gmail.com", branch="CSE", semester=7, section="B"))
	db.session.add(Student(usn = "01FB15ECS017", name="Prasanna Rajan", email="prasanna.rajan@gmail.com", branch="CSE", semester=5, section="B"))
	db.session.add(Student(usn = "01FB15ECS018", name="Yasser Nizam", email="yasser.nizam@gmail.com", branch="CSE", semester=3, section="B"))
	db.session.add(Student(usn = "01FB15ECS019", name="Rakshit Sinha", email="rakshit.sinha@gmail.com", branch="CSE", semester=5, section="B"))
	db.session.add(Student(usn = "01FB15ECS020", name="Gaurav Kothari", email="gaurav.kothari@gmail.com", branch="CSE", semester=3, section="B"))
	db.session.add(Student(usn = "01FB15ECS021", name="Arjun Singh Mann", email="arjun.singh.mann@gmail.com", branch="CSE", semester=5, section="C"))
	db.session.add(Student(usn = "01FB15ECS022", name="Anant Singh Mann", email="anant.singh.mann@gmail.com", branch="CSE", semester=3, section="C"))
	db.session.add(Student(usn = "01FB15ECS023", name="Josh Pasricha", email="josh.pasricha@gmail.com", branch="CSE", semester=5, section="C"))
	db.session.add(Student(usn = "01FB15ECS024", name="Dilsher Brar", email="dilsher.brar@gmail.com", branch="CSE", semester=3, section="C"))
	db.session.add(Student(usn = "01FB15ECS025", name="Saksham Arya", email="saksham.arya@gmail.com", branch="CSE", semester=5, section="C"))
	db.session.add(Student(usn = "01FB15ECS026", name="Yash Upadhyay", email="yash.upadhyay@gmail.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn = "01FB15ECS027", name="Abhinav Kejriwal", email="abhinav.kejriwal@gmail.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn = "01FB15ECS028", name="Yash Mathur", email="yash.mathur@gmail.com", branch="CSE", semester=3, section="C"))
	db.session.add(Student(usn = "01FB15ECS029", name="Varuni Sutrave", email="varunisutrave4@gmail.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn = "01FB15ECS310", name="Srishti Mishra", email="srishtimishra56@gmail.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn = "01FB15ECS000", name="Test Student", email="captain.se6@gmail.com", branch="CSE", semester=7, section="C"))
	db.session.commit()

def teacher_data():
	"""Seeds the Teacher Table."""
	db.session.add(Teacher(f_id = "F001", name="Anirudh Heda", email="anirudh.heda@gmail.com", branch="CSE", position="Head of Department"))
	db.session.add(Teacher(f_id = "F002", name="Yash Agarwal", email="yash.agarwal@gmail.com", branch="CSE", position="Assistant Professor"))
	db.session.add(Teacher(f_id = "F003", name="Saket Marodia", email="saket.marodia@gmail.com", branch="CSE", position="Professor"))
	db.session.add(Teacher(f_id = "F004", name="Vinay Somani", email="vinay.somani@gmail.com", branch="CSE", position="Assistant Professor"))
	db.session.add(Teacher(f_id = "F005", name="Sumangal Bhaiya", email="sumangal.bhiya@gmail.com", branch="CSE", position="Assistant Professor"))
	db.session.add(Teacher(f_id = "F006", name="Akash Boob", email="akash.boob@gmail.com", branch="CSE", position="Assistant Professor"))
	db.session.add(Teacher(f_id = "F007", name="Kishan Soni", email="kishan.soni@gmail.com", branch="CSE", position="Professor"))
	db.session.add(Teacher(f_id = "F008", name="Sarthak Banka", email="sarthak.banka@gmail.com", branch="CSE", position="Assistant Professor"))
	db.session.add(Teacher(f_id = "F009", name="Kritagya Jain", email="kritagya.jain@gmail.com", branch="CSE", position="Assistant Professor"))
	db.session.commit()

def coursebase_data():
	"""Seeds the CourseBase Table."""
	db.session.add(CourseBase(course_name = "Data Structures", course_code = "UE15CS201", description = "Arrays, Linked lists, Trees", semester = 3, branch = "CSE", no_of_max_members = 3, calendar_id = "xyz"))
	db.session.add(CourseBase(course_name = "Algorithm Design", course_code = "UE15CS202", description = "Sorting algorithms, Brute force, Divide and Conquor", semester = 3, branch = "CSE", no_of_max_members = 3, calendar_id = "xyz"))
	db.session.add(CourseBase(course_name = "Introduction to Data Science", course_code = "UE15CS203", description = "Study of differnt data analytics methods", semester = 3, branch = "CSE", no_of_max_members = 3, calendar_id = "xyz"))
	db.session.add(CourseBase(course_name = "Operating Systems", course_code = "UE15CS301", description = "Paging, Disk Reading, File Storage, Race Conditions, Threads, Deadlocks", semester = 5, branch = "CSE", no_of_max_members = 3, calendar_id = "xyz"))
	db.session.add(CourseBase(course_name = "Database Management Systems", course_code = "UE15CS302", description = "Creating, Maintaining and modifying Databses", semester = 5, branch = "CSE", no_of_max_members = 3, calendar_id = "xyz"))
	db.session.add(CourseBase(course_name = "Computer Networks", course_code = "UE15CS303", description = "Study of all the layers in networking", semester = 5, branch = "CSE", no_of_max_members = 3, calendar_id = "xyz"))
	db.session.add(CourseBase(course_name = "Theory of computation", course_code = "UE15CS401", description = "Study of the working of automatas", semester = 7, branch = "CSE", no_of_max_members = 3, calendar_id = "xyz"))
	db.session.add(CourseBase(course_name = "Web Technologies", course_code = "UE15CS402", description = "Creating and maintaining basic sites", semester = 7, branch = "CSE", no_of_max_members = 3, calendar_id = "xyz"))
	db.session.add(CourseBase(course_name = "Machine Learning", course_code = "UE15CS403", description = "Understanding the elementary parts of Machine Learning", semester = 7, branch = "CSE", no_of_max_members = 3, calendar_id = "xyz"))
	db.session.commit()

def course_data():
	"""Seeds the Course Table."""
	db.session.add(Course(course_code = "UE15CS201", deliverables = "Creation of a working Binary Search Tree", deliverable_deadline = "2018-11-30"))
	db.session.add(Course(course_code = "UE15CS202", deliverables = "Study the speeds of multiple sorting algorithms", deliverable_deadline = "2018-11-29"))
	db.session.add(Course(course_code = "UE15CS203", deliverables = "Study and list the teams in order of probability of winning in IPL", deliverable_deadline = "2018-11-28"))
	db.session.add(Course(course_code = "UE15CS301", deliverables = "Finding the current date and time from the terminal", deliverable_deadline = "2018-11-30"))
	db.session.add(Course(course_code = "UE15CS302", deliverables = "Creating and managing a Resaturant Database", deliverable_deadline = "2018-11-29"))
	db.session.add(Course(course_code = "UE15CS303", deliverables = "Making an algorithm to find the shortest distance to a router from another in a a mesh of routers", deliverable_deadline = "2018-11-28"))
	db.session.add(Course(course_code = "UE15CS401", deliverables = "Make an automata for a slot machine with code", deliverable_deadline = "2018-11-30"))
	db.session.add(Course(course_code = "UE15CS402", deliverables = "Creating a well defined dynamic website", deliverable_deadline = "2018-11-29"))
	db.session.add(Course(course_code = "UE15CS403", deliverables = "Make a system to predict the kind of song that is played", deliverable_deadline = "2018-11-28"))
	db.session.commit()

def team_data():
	"""Seeds the Team Table."""
	




