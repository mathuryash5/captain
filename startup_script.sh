#!/bin/sh
sudo /etc/init.d/postgresql restart
python3 manage.py recreate-db
python3 manage.py seed-db
export FLASK_ENV=development