from app import db
from app.models import User, Student, Teacher, CourseBase, Course, Team


def student_data():
	"""Seeds the Student Table."""
	db.session.add(Student(usn = "01FB15ECS001", name="Aditya Ramani", email="aditya.ramani@gmail.com", branch="CSE", semester=7, section="A"))
	db.session.add(Student(usn = "01FB15ECS002", name="Anvith Shetty", email="anvith.shetty@gmail.com", branch="CSE", semester=7, section="A"))
	db.session.add(Student(usn = "01FB15ECS003", name="Saket Golyan", email="saket.golyan@gmail.com", branch="CSE", semester=7, section="A"))
	db.session.add(Student(usn = "01FB15ECS004", name="Advait Jha", email="advait.jha@gmail.com", branch="CSE", semester=5, section="A"))
	db.session.add(Student(usn = "01FB15ECS005", name="Atharva Matta", email="atharva.matta@gmail.com", branch="CSE", semester=5, section="A"))
	db.session.add(Student(usn = "01FB15ECS006", name="Aditya Vir Roy", email="aditya.vir.roy@gmail.com", branch="CSE", semester=5, section="A"))
	db.session.add(Student(usn = "01FB15ECS007", name="Anirudh Gupta", email="anirudh.gupta@gmail.com", branch="CSE", semester=3, section="A"))
	db.session.add(Student(usn = "01FB15ECS008", name="Anubhav Agarwal", email="anubhav.agarwal@gmail.com", branch="CSE", semester=3, section="A"))
	db.session.add(Student(usn = "01FB15ECS009", name="Rohan Agarwal", email="rohan.agarwal@gmail.com", branch="CSE", semester=3, section="A"))
	db.session.add(Student(usn = "01FB15ECS010", name="Aayushman Arora", email="aayushman.arora@gmail.com", branch="CSE", semester=7, section="B"))
	db.session.add(Student(usn = "01FB15ECS011", name="Rahil Arora", email="rahil.arora@gmail.com", branch="CSE", semester=7, section="B"))
	db.session.add(Student(usn = "01FB15ECS012", name="Armaan Imaam", email="armaan.imaam@gmail.com", branch="CSE", semester=7, section="B"))
	db.session.add(Student(usn = "01FB15ECS013", name="Aditya Gandhi", email="aditya.gandhi@gmail.com", branch="CSE", semester=5, section="B"))
	db.session.add(Student(usn = "01FB15ECS014", name="Mrigank Khemka", email="mrigank.khemka@gmail.com", branch="CSE", semester=5, section="B"))
	db.session.add(Student(usn = "01FB15ECS015", name="Vatsal Agarwal", email="vatsal.agarwal@gmail.com", branch="CSE", semester=5, section="B"))
	db.session.add(Student(usn = "01FB15ECS016", name="Prasanna Rajan", email="prasanna.rajan@gmail.com", branch="CSE", semester=3, section="B"))
	db.session.add(Student(usn = "01FB15ECS017", name="Yasser Nizam", email="yasser.nizam@gmail.com", branch="CSE", semester=3, section="B"))
	db.session.add(Student(usn = "01FB15ECS018", name="Gaurav Kothari", email="gaurav.kothari@gmail.com", branch="CSE", semester=3, section="B"))
	db.session.add(Student(usn = "01FB15ECS019", name="Yash Mathur", email="yash.mathur@gmail.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn = "01FB15ECS020", name="Varuni Sutrave", email="varuni.sutrave@gmail.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn = "01FB15ECS021", name="Srishti Mishra", email="srishti.mishra@gmail.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn = "01FB15ECS022", name="Saksham Arya", email="saksham.arya@gmail.com", branch="CSE", semester=5, section="C"))
	db.session.add(Student(usn = "01FB15ECS023", name="Josh Pasricha", email="josh.pasricha@gmail.com", branch="CSE", semester=5, section="C"))
<<<<<<< HEAD
	db.session.add(Student(usn = "01FB15ECS024", name="Arjun Singh Mann", email="arjun.singh.mann@gmail.com", branch="CSE", semester=5, section="C"))
	db.session.add(Student(usn = "01FB15ECS025", name="Anant Singh Mann", email="anant.singh.mann@gmail.com", branch="CSE", semester=3, section="C"))
	db.session.add(Student(usn = "01FB15ECS026", name="Dilsher Brar", email="dilsher.brar@gmail.com", branch="CSE", semester=3, section="C"))
	db.session.add(Student(usn = "01FB15ECS027", name="Abhinav Kejriwal", email="abhinav.kejriwal@gmail.com", branch="CSE", semester=3, section="C"))
=======
	db.session.add(Student(usn = "01FB15ECS024", name="Dilsher Brar", email="dilsher.brar@gmail.com", branch="CSE", semester=3, section="C"))
	db.session.add(Student(usn = "01FB15ECS025", name="Saksham Arya", email="saksham.arya@gmail.com", branch="CSE", semester=5, section="C"))
	db.session.add(Student(usn = "01FB15ECS026", name="Yash Upadhyay", email="yash.upadhyay@gmail.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn = "01FB15ECS027", name="Abhinav Kejriwal", email="abhinav.kejriwal@gmail.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn = "01FB15ECS028", name="Yash Mathur", email="yash.mathur@gmail.com", branch="CSE", semester=3, section="C"))
	db.session.add(Student(usn = "01FB15ECS029", name="Varuni Sutrave", email="varunisutrave4@gmail.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn = "01FB15ECS310", name="Srishti Mishra", email="srishtimishra56@gmail.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn = "01FB15ECS000", name="Test Student", email="captain.se6@gmail.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn = "01FB15ECS341", name="Aria Ly", email="air72659@gmail.com", branch="CSE", semester=7, section="C"))
	db.session.add(Student(usn = "01FB15ECS346", name="Neha H", email="srishtimishra@pesu.pes.edu", branch="CSE", semester=7, section="C"))
>>>>>>> 87ae59fc631b30ab3a35b839b934c5e7a0790e48
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
	db.session.add(Course(course_code = "UE15CS201", deliverables = "Creation of a working Binary Search Tree", deliverable_deadline = "2018-11-30", teacher_resources = "xyz.com"))
	db.session.commit()
	db.session.add(Course(course_code = "UE15CS202", deliverables = "Study the speeds of multiple sorting algorithms", deliverable_deadline = "2018-11-29", teacher_resources = "xyz.com"))
	db.session.commit()
	db.session.add(Course(course_code = "UE15CS203", deliverables = "Study and list the teams in order of probability of winning in IPL", deliverable_deadline = "2018-11-28", teacher_resources = "xyz.com"))
	db.session.commit()
	db.session.add(Course(course_code = "UE15CS301", deliverables = "Finding the current date and time from the terminal", deliverable_deadline = "2018-11-30", teacher_resources = "xyz.com"))
	db.session.commit()
	db.session.add(Course(course_code = "UE15CS302", deliverables = "Creating and managing a Resaturant Database", deliverable_deadline = "2018-11-29", teacher_resources = "xyz.com"))
	db.session.commit()
	db.session.add(Course(course_code = "UE15CS303", deliverables = "Making an algorithm to find the shortest distance to a router from another in a a mesh of routers", deliverable_deadline = "2018-11-28", teacher_resources = "xyz.com"))
	db.session.commit()
	db.session.add(Course(course_code = "UE15CS401", deliverables = "Make an automata for a slot machine with code", deliverable_deadline = "2018-11-30", teacher_resources = "xyz.com"))
	db.session.commit()
	db.session.add(Course(course_code = "UE15CS402", deliverables = "Creating a well defined dynamic website", deliverable_deadline = "2018-11-29", teacher_resources = "xyz.com"))
	db.session.commit()
	db.session.add(Course(course_code = "UE15CS403", deliverables = "Make a system to predict the kind of song that is played", deliverable_deadline = "2018-11-28", teacher_resources = "xyz.com"))
	db.session.commit()

def team_data():
	"""Seeds the Team Table."""
	db.session.add(Team(course_code = "UE15CS201", session_id = "1", usn_list = "{member_1 : Anirudh Gupta, member_2 : Anubhav Agarwal, member_3 : Rohan Agarwal}", github_user = "Anirudh Gupta", github_repo = "https://github.com/AnirudhGupta/captain"))
	db.session.add(Team(course_code = "UE15CS201", session_id = "2", usn_list = "{member_1 : Prasanna Rajan, member_2 : Yasser Nizam, member_3 : Gaurav Kothari}", github_user = "Prasanna Rajan", github_repo = "https://github.com/PrasannaRajan/captain"))
	db.session.add(Team(course_code = "UE15CS201", session_id = "3", usn_list = "{member_1 : Anant Singh Mann, member_2 : Dilsher Brar, member_3 : Abhinav Kejriwal}", github_user = "Anant Singh Mann", github_repo = "https://github.com/AnantSinghMann/captain"))
	db.session.add(Team(course_code = "UE15CS202", session_id = "4", usn_list = "{member_1 : Anirudh Gupta, member_2 : Anubhav Agarwal, member_3 : Rohan Agarwal}", github_user = "Anirudh Gupta", github_repo = "https://github.com/AnirudhGupta/captain"))
	db.session.add(Team(course_code = "UE15CS202", session_id = "5", usn_list = "{member_1 : Prasanna Rajan, member_2 : Yasser Nizam, member_3 : Gaurav Kothari}", github_user = "Prasanna Rajan", github_repo = "https://github.com/PrasannaRajan/captain"))
	db.session.add(Team(course_code = "UE15CS202", session_id = "6", usn_list = "{member_1 : Anant Singh Mann, member_2 : Dilsher Brar, member_3 : Abhinav Kejriwal}", github_user = "Anant Singh Mann", github_repo = "https://github.com/AnantSinghMann/captain"))
	db.session.add(Team(course_code = "UE15CS203", session_id = "7", usn_list = "{member_1 : Anirudh Gupta, member_2 : Anubhav Agarwal, member_3 : Rohan Agarwal}", github_user = "Anirudh Gupta", github_repo = "https://github.com/AnirudhGupta/captain"))
	db.session.add(Team(course_code = "UE15CS203", session_id = "8", usn_list = "{member_1 : Prasanna Rajan, member_2 : Yasser Nizam, member_3 : Gaurav Kothari}", github_user = "Prasanna Rajan", github_repo = "https://github.com/PrasannaRajan/captain"))
	db.session.add(Team(course_code = "UE15CS203", session_id = "9", usn_list = "{member_1 : Anant Singh Mann, member_2 : Dilsher Brar, member_3 : Abhinav Kejriwal}", github_user = "Anant Singh Mann", github_repo = "https://github.com/AnantSinghMann/captain"))
	db.session.add(Team(course_code = "UE15CS301", session_id = "10", usn_list = "{member_1 : Advait Jha, member_2 : Atharva Matta, member_3 : Aditya Vir Roy}", github_user = "Advait Jha", github_repo = "https://github.com/AdvaitJha/captain"))
	db.session.add(Team(course_code = "UE15CS301", session_id = "11", usn_list = "{member_1 : Aditya Gandhi, member_2 : Mrigank Khemka, member_3 : Vatsal Agarwal}", github_user = "Aditya Gandhi", github_repo = "https://github.com/AdityaGandhi/captain"))
	db.session.add(Team(course_code = "UE15CS301", session_id = "12", usn_list = "{member_1 : Saksham Arya, member_2 : Josh Pasricha, member_3 : Arjun Singh Mann}", github_user = "Josh Pasricha", github_repo = "https://github.com/JoshPasricha/captain"))
	db.session.add(Team(course_code = "UE15CS302", session_id = "13", usn_list = "{member_1 : Advait Jha, member_2 : Atharva Matta, member_3 : Aditya Vir Roy}", github_user = "Advait Jha", github_repo = "https://github.com/AdvaitJha/captain"))
	db.session.add(Team(course_code = "UE15CS302", session_id = "14", usn_list = "{member_1 : Aditya Gandhi, member_2 : Mrigank Khemka, member_3 : Vatsal Agarwal}", github_user = "Aditya Gandhi", github_repo = "https://github.com/AdityaGandhi/captain"))
	db.session.add(Team(course_code = "UE15CS302", session_id = "15", usn_list = "{member_1 : Saksham Arya, member_2 : Josh Pasricha, member_3 : Arjun Singh Mann}", github_user = "Josh Pasricha", github_repo = "https://github.com/JoshPasricha/captain"))
	db.session.add(Team(course_code = "UE15CS303", session_id = "16", usn_list = "{member_1 : Advait Jha, member_2 : Atharva Matta, member_3 : Aditya Vir Roy}", github_user = "Advait Jha", github_repo = "https://github.com/AdvaitJha/captain"))
	db.session.add(Team(course_code = "UE15CS303", session_id = "17", usn_list = "{member_1 : Aditya Gandhi, member_2 : Mrigank Khemka, member_3 : Vatsal Agarwal}", github_user = "Aditya Gandhi", github_repo = "https://github.com/AdityaGandhi/captain"))
	db.session.add(Team(course_code = "UE15CS303", session_id = "18", usn_list = "{member_1 : Saksham Arya, member_2 : Josh Pasricha, member_3 : Arjun Singh Mann}", github_user = "Josh Pasricha", github_repo = "https://github.com/JoshPasricha/captain"))
	db.session.add(Team(course_code = "UE15CS401", session_id = "19", usn_list = "{member_1 : Aditya Ramani, member_2 : Anvith Shetty, member_3 : Saket Golyan}", github_user = "Aditya Ramani", github_repo = "https://github.com/AdityaRamani/captain"))
	db.session.add(Team(course_code = "UE15CS401", session_id = "20", usn_list = "{member_1 : Aayushman Arora, member_2 : Rahil Arora ,member_3 : Armaan Imaam}", github_user = "Rahil Arora", github_repo = "https://github.com/RahilArora/captain"))
	db.session.add(Team(course_code = "UE15CS401", session_id = "21", usn_list = "{member_1 : Yash Mathur, member_2 : Varuni Sutrave, member_3 : Srishti Mishra}", github_user = "Yash Mathur", github_repo = "https://github.com/mathuryash5/captain"))
	db.session.add(Team(course_code = "UE15CS402", session_id = "22", usn_list = "{member_1 : Aditya Ramani, member_2 : Anvith Shetty, member_3 : Saket Golyan}", github_user = "Aditya Ramani", github_repo = "https://github.com/AdityaRamani/captain"))
	db.session.add(Team(course_code = "UE15CS402", session_id = "23", usn_list = "{member_1 : Aayushman Arora, member_2 : Rahil Arora ,member_3 : Armaan Imaam}", github_user = "Rahil Arora", github_repo = "https://github.com/RahilArora/captain"))
	db.session.add(Team(course_code = "UE15CS402", session_id = "24", usn_list = "{member_1 : Yash Mathur, member_2 : Varuni Sutrave, member_3 : Srishti Mishra}", github_user = "Yash Mathur", github_repo = "https://github.com/mathuryash5/captain"))
	db.session.add(Team(course_code = "UE15CS403", session_id = "25", usn_list = "{member_1 : Aditya Ramani, member_2 : Anvith Shetty, member_3 : Saket Golyan}", github_user = "Aditya Ramani", github_repo = "https://github.com/AdityaRamani/captain"))
	db.session.add(Team(course_code = "UE15CS403", session_id = "26", usn_list = "{member_1 : Aayushman Arora, member_2 : Rahil Arora ,member_3 : Armaan Imaam}", github_user = "Rahil Arora", github_repo = "https://github.com/RahilArora/captain"))
	db.session.add(Team(course_code = "UE15CS403", session_id = "27", usn_list = "{member_1 : Yash Mathur, member_2 : Varuni Sutrave, member_3 : Srishti Mishra}", github_user = "Yash Mathur", github_repo = "https://github.com/mathuryash5/captain"))
