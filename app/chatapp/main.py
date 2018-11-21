from flask_socketio import SocketIO, emit, join_room, leave_room

from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(data, methods=['GET', 'POST']):
    print('received my event: ' + str(data))
    socketio.emit('my response', {'user_name': data['user_name'],'message': data['message']}, room=data['room'], callback=messageReceived)

@socketio.on('joined')
def joined(data):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    print(str(data))
    room = data['room']
    join_room(room)
    emit('my response', {'user_name': data['user_name'], 'message': 'has joined'}, room=room)

@socketio.on('left')
def left(data):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = data['room']
    leave_room(room)
    print(left)
    emit('my response', {'user_name': data['user_name'], 'message': 'has left'}, room=room)


@socketio.on('my broadcast event')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Is Connected'})
    # emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True, port=8000, certfile='server.crt', keyfile='server.key')