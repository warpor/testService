#!/bin/sh
# Collect static files
# Apply database migrations


if [ ! -f .env ]
then
  export $(cat .env | xargs)
fi

echo $DB_HOST
python /code/tests_service/manage.py migrate

echo "from django.contrib.auth.models import User; User.objects.create_superuser('${ADMIN_NAME}',
 'admin@example.com', '${ADMIN_PASSWORD}')" | python /code/tests_service/manage.py shell

python /code/tests_service/manage.py runserver 0.0.0.0:8000
