from flask import Flask, redirect,url_for,request,render_template
import requests
import get_request
from flask_cors import CORS
import json
import addToDatabase
import verifyDatabase

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


@app.route("/<URL>")
def decide(URL):
    DB_response = ""
    if URL[0] == "R" and URL[1]=="E" and URL[2]=="Q":
        DB_response = get_request.get(URL[4:])
        return DB_response
    elif URL[0] == "A" and URL[1]=="D" and URL[2]=="D":
        DB_response = addToDatabase.add(URL[4:])
        return str(DB_response)
    elif URL[0] == "V" and URL[1]=="R" and URL[2]=="F":
        DB_response = verifyDatabase.verify(URL[4:])
        return str(DB_response)

app.run()
