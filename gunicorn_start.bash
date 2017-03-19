#!/bin/bash

NAME="uavlook_rebuild"                                    # Name of the application
DJANGODIR=/home/ubuntu/uavlook/uavlook                    # Django project directory
SOCKFILE=/var/sock/uavlook.sock  # we will communicte using this unix socket
USER=ubuntu                                        # the user to run as
GROUP=webapps                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=uavlook.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=uavlook.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/ubuntu/uavlook/env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
echo PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/ubuntu/uavlook/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --bind=unix:$SOCKFILE \
    --log-level=info \
    --log-file=/home/ubuntu/uavlook/logs/gunicorn.log
gunicorn_start (END)

