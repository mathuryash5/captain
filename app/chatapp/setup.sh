#!/bin/sh
virtualenv -p python3 chat
source chat/bin/activate
pip3 install flask, flask_socketio, eventlet
