#!/usr/bin/env sh
gunicorn -b 0.0.0.0:8080 app:application --reload --access-logfile -
