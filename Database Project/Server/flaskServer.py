from flask import Flask, redirect,url_for,request,render_template
import requests
import get_request
from flask_cors import CORS

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
    #if the URL contains the YT code
    if URL[0] == "R" and URL[1]=="E" and URL[2]=="Q":
        DB_response = get_request.get(URL[4:])
    return str(DB_response)

app.run()
