from flask import Flask, Response, jsonify
import time
from celery import Celery
import json

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

app = Flask(__name__)

celery = Celery(
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND
)

celery.conf.update(app.config)

current_tasks = []

@celery.task
def long_task():
    counter = 0
    for i in range(10):
        counter += 1
        time.sleep(1)

    print(f"End long task {counter}")


@app.route("/start", methods=["PUT"])
def start_pipeline():
    print("Start long task")
    current_tasks.append(long_task.delay())
    return {"pipeline": "started"}, 201


@app.route("/status", methods=["GET"])
def get_status(id=None):
    res = list()
    for task in current_tasks:
        print(type(task.id))
        print(type(task.state))
        print(f"{task.id} => {task.state}")
        res.append({task.id: task.state})
    print(type(res))
    return jsonify(res)


application = app
