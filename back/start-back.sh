#!/usr/bin/env sh
gunicorn -b 0.0.0.0:8081 app:application --reload --access-logfile -
