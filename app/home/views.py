from flask import jsonify, request, render_template
from flask import redirect, url_for, session
from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin
from flask import Response, make_response

from . import home
from .. import student, teacher


from requests.exceptions import HTTPError
import simplejson as json
import datetime

from sqlalchemy import exc

from app import login_manager
from app.models import User, Student, Teacher

from .. import db

from app.login import get_google_auth, checkUser, Auth
'''
    Load homepage
'''
@home.route('/', methods=['GET'])
def index():
    return render_template('index.html')

'''
    Test
'''
@home.route('/hi', methods = ['GET', 'POST'])
@login_required
def hi():
    response_object = {
    'status': 'success',
    'message': 'HI'
    }
    return jsonify(response_object)

'''
    Saves state on user login
'''
@home.route('/login', methods=['GET','POST'])
def login():
    print("in login")
    print(current_user)
    try:
        if current_user.is_authenticated:
            print(current_user.name," ", current_user.email, "is authenticated!")
            response_object = {
            'status': 'success',
            'message': 'Already logged in.'
            }
            u, isTeacher = checkUser(current_user.email)
            if isTeacher:
                return render_template("Teacher.html")
            else:
                return render_template("dashboard.html")
            # Check if current_user is teacher or student
            return jsonify(response_object)
            #return redirect(url_for('users.index'))
    except:
        print("current user")
    print("get auth")
    google = get_google_auth()
    auth_url, state = google.authorization_url(
        Auth.AUTH_URI, access_type='offline')
    print(auth_url, state)
    session['oauth_state'] = state
    return render_template('login.html', auth_url=auth_url)


'''
    Authenticates google login with DB and saves current user
'''
@home.route('/gCallback', methods=['GET','POST'])
def callback():
    # Redirect user to home page if already logged in.
    print("in gcallback!")
    if current_user is not None and current_user.is_authenticated:
        print("is auth already")
        u, isTeacher = checkUser(current_user.email)
        if isTeacher:
            print("Displaying the Teacher dashboard")
            user_info = db.session.query(Teacher).filter(Teacher.email == current_user.email).first()
            courses_taken = user_info.course_to_section.keys()
            print("="*30)
            print(user_info)
            # print(all_course_names)
            print("="*30)
            response = {"teacher_name" : user_info.name, "courses_taken" : courses_taken, "course_to_section" : user_info.course_to_section}
            return render_template("Teacher.html", response = response)

        else:
            user_info = db.session.query(Student).filter(Student.email == current_user.email).first()
            course_names = db.session.query(CourseBase.course_name).filter(CourseBase.semester == user_info.semester)
            all_course_names = db.session.query(CourseBase.course_name).all()
            print("="*30)
            print(user_info)
            print(user_info.semester)
            print(user_info.lab_marks)
            # print(course_names)
            print(all_course_names)
            print("="*30)
            response = {"student_name" : user_info.name, "lab_marks" : user_info.lab_marks, "course_names" : course_names}
            return render_template("dashboard.html", response = response)
    if 'error' in request.args:
        print("some error")
        if request.args.get('error') == 'access_denied':
            return 'You denied access.'
        return 'Error encountered.'
    if 'code' not in request.args and 'state' not in request.args:
        print("missing?")
        return render_template('index.html')
    else:
        print("trying?")
        # Execution reaches here when user has
        # successfully authenticated our app.
        google = get_google_auth(state=session['oauth_state'])
        try:
            token = google.fetch_token(
                Auth.TOKEN_URI,
                client_secret=Auth.CLIENT_SECRET,
                authorization_response=request.url)
            print(token)
        except HTTPError:
            return 'HTTPError occurred.'
        google = get_google_auth(token=token)
        resp = google.get(Auth.USER_INFO)
        if resp.status_code == 200:
            user_data = resp.json()
            # print(user_data)
            email = user_data['email']
            print(email)
            user, isTeacher = checkUser(email)
            

            # user = User.query.filter_by(email=email).first()
            print(email)
            print(user)
            if user is None:
                print("New user! need Details?")
                response_object = {
                'status': 'fail',
                'message': 'Not authorized! Contact admin for further information.'
                }
                return jsonify(response_object)
            # try:
            # current_user.is_authenticated = True
            current_user.name = user_data['name']
            current_user.email = user_data['email']
            current_user.tid = 2
            # current_user.token = token
            login_user(user)
            # except: 
            #     print("Error adding user details and logging in")
            #     return 'Error adding user details and logging in'
            if isTeacher:
                print("Displaying the Teacher dashboard")
                user_info = db.session.query(Teacher).filter(Teacher.email == current_user.email).first()
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
            else:
                print("Displaying the Student dashboard")
                user_info = db.session.query(Student).filter(Student.email == current_user.email).first()
                course_names = db.session.query(CourseBase.course_name).filter(CourseBase.semester == user_info.semester)
                all_course_names = db.session.query(CourseBase.course_name).all()
                print("="*30)
                print(user_info)
                print(user_info.semester)
                print(user_info.lab_marks)
                print(course_names)
                # print(all_course_names)
                print("="*30)
                response = {"student_name" : user_info.name, "lab_marks" : user_info.lab_marks, "course_names" : course_names}
                return render_template("dashboard.html", response = response)

        return 'Could not fetch your information.'

@home.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    # db.session.add(user)
    # db.session.commit()
    logout_user()
    return redirect(url_for('index.html'))


@home.route("/chat/<courseid>", methods=["GET"])
@login_required
def chat(courseid):
    # Find which team id from querying current_user.has_team for courseid's teamValue.
    teamID = random.randint(1,2)
    response = make_response(render_template('chat.html'))
    response.set_cookie('tid', str(teamID), max_age=60*5)
    response.set_cookie('usn', str(current_user.email), max_age=60*5)
    return response
    # return redirect("http://localhost:")
    # return jsonify({'name': current_user.email })