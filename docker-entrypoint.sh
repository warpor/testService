#!/bin/sh
# Collect static files
# Apply database migrations
echo "Apply database migrations"

python /code/tests_service/manage.py migrate
#python tests_service/manage.py migrate testing 0002
#python tests_service/manage.py migrate testing 0003

python /code/tests_service/manage.py runserver
