#!/bin/sh

if [ "$DATABASE" = "mariadb" ]
then
    echo "Waiting for mariadb..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "MariaDB started"
fi

python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate

exec "$@"