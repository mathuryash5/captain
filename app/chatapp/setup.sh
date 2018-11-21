#!/bin/sh
DIRECTORY='chat'
if [ ! -d "$DIRECTORY" ]; then
	echo 'creating venv chat'
	virtualenv -p python3 chat
	sudo pip3 install flask, flask_socketio
fi

# run 
# $ source chat/bin/activate to start virtual env