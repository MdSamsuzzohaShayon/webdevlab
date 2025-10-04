#!/bin/bash

# Delete previous virtual environment if there is any
deactivate
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
nano .env
./manage.py makemigrations
./manage.py migrate --run-syncdb
./manage.py runserver

