#!/bin/bash

if [ -e "/run/nginx.pid" ]
then
	nginx -s reload
else
	nginx
fi

#gunicorn -b ask-klyukvin.io:8000 ask-klyukvin.wsgi
gunicorn -c ask-klyukvin/gunicorn_conf.py ask-klyukvin.wsgi

nginx -s stop
