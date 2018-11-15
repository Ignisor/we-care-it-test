#!/bin/sh

echo "Apply database migrations"
python3 manage.py migrate

echo "Collecting static"
python3 manage.py collectstatic --noinput

exec "$@"
