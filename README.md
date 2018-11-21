# Captain
A mini-project and lab monitoring system for students and teachers to facilitate mini-project tracking and grading, course content management, student-teacher communication and interactive quizzes

## To run    
      
Note: If your gmail id does not exist in init_data.py, you cannot sign in. Add it if necessary.  
   
Start up postgres database   
$ ./startup.sh   
   
Initialize node modules in app/static   
$ cd app/static   
$ npm install   

Run the app   
$ python3 manage.py run --cert app/ssl/server.crt --key app/ssl/server.key
   
For chat functionality (separate server), open a new terminal and go to app/chatapp
$ cd app/chatapp   

Create a virtual env using the setup script   
$ ./setup.sh   
   
Run the chat server   
$ python3 main.py
