from flask import jsonify, request, render_template
from flask import redirect, url_for, session
from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin
from flask import Response, make_response

from . import home
from .. import student, teacher

from requests_oauthlib import OAuth2Session
from requests.exceptions import HTTPError
import simplejson as json
import datetime

from sqlalchemy import exc

from app import login_manager
from app.models import User, Student, Teacher

from .. import db

# Google Auth API details
class Auth:
    CLIENT_ID = ('630861931474-mqa933274lsoctu9r94rb0j4tas2o6r6.apps.googleusercontent.com')
    CLIENT_SECRET = 'gUOr5-q89miUNIwEtTciEC2f'
    REDIRECT_URI = 'https://localhost:5000/gCallback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://www.googleapis.com/oauth2/v3/token'
    USER_INFO = 'https://www.googleapis.com/plus/v1/people/me/openIdConnect'
    # USER_INFO = 'https://www.googleapis.com/oauth2/v3/userinfo?alt=json'
    SCOPE = ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
    #USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'



'''
    Creates OAuth session object, used by login functions below
'''
@login_manager.user_loader
def load_user(email):
    print(email)
    u, isTeacher = checkUser(email)
    return u

def get_google_auth(state=None, token=None):
    if token:
        return OAuth2Session(Auth.CLIENT_ID, token=token)
    if state:
        return OAuth2Session(
            Auth.CLIENT_ID,
            state=state,
            redirect_uri=Auth.REDIRECT_URI)
    oauth = OAuth2Session(
        Auth.CLIENT_ID,
        redirect_uri=Auth.REDIRECT_URI,
        scope=Auth.SCOPE)
    return oauth

def checkUser(userEmail):
    try:
        print("Are you a teacher?")
        user = db.session.query(Teacher).filter(Teacher.email==userEmail).first()
        print(user)
        if user:
            print("Is a teacher")
            return user, 1
        else:
            try:
                print("Are you a student?")
                user = db.session.query(Student).filter(Student.email==userEmail).first()
                if user:
                    print("Is a student")
                    return user, 0
            except:
                print("Error querying student information")
    except:
        print("Error querying teacher information")

        

    return -1

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
            return render_template("Teacher.html")
        else:
            return render_template("dashboard.html")
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
                return render_template("Teacher.html")
            else:
                return render_template("dashboard.html")

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
    teamID = "2"
    response = make_response(render_template('chat.html'))
    response.set_cookie('tid', str(teamID), max_age=60*2)
    return response
    # return redirect("http://localhost:")
    # return jsonify({'name': current_user.email })