from flask import Flask
import requests

app = Flask(__name__)


@app.route("/pipeline", methods=["PUT"])
def start_pipeline():
    req = requests.put("http://back:8081/start", json={"pipeline": "start"})
    print(req.status_code)
    return req.json(), req.status_code


@app.route("/pipeline", methods=["GET"])
def get_status():
    req = requests.get("http://back:8081/status")
    return req.content, req.status_code


application = app
