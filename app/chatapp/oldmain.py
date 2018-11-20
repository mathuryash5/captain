import socketio
from flask import Flask, render_template

sio = socketio.Server(async_mode='threading')
chatapp = Flask(__name__)
chatapp.wsgi = socketio.Middleware(sio, chatapp.wsgi_app)


@chatapp.route('/', methods=['GET','POST'])
def index():
    """Serve the client-side application."""
    return render_template('session.html')

@sio.on('connect', namespace='/chat')
def connect(sid, environ):
    print("connect ", sid)

@sio.on('chat message', namespace='/chat')
def message(sid, data):
    print("message ", data)
    sio.emit('reply', room=sid)

@sio.on('disconnect', namespace='/chat')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # wrap Flask application with engineio's middleware
    chatapp.run(threaded='true', port=8000, debug=True, ssl_context=('server.crt', 'server.key'))

   



# from flask import Flask, render_template
# from flask_socketio import SocketIO

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
# socketio = SocketIO(app)

# @app.route('/')
# def sessions():
#     return render_template('session.html')

# def messageReceived(methods=['GET', 'POST']):
#     print('message was received!!!')

# @socketio.on('my event')
# def handle_my_custom_event(json, methods=['GET', 'POST']):
#     print('received my event: ' + str(json))
#     socketio.emit('my response', json, callback=messageReceived)

# if __name__ == '__main__':
#     socketio.run(app, debug=True, port=1234)