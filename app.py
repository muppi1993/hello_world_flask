from flask import Flask
from flask import url_for
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/login")
def login_page():
    # Process login
    return 'Hello, User!'

@app.route("/login2/<user>")
def login_user(user):
    # User login flow.
    return user

@app.route("/print")
def redirect_to_login():
    return url_for('login_user',user='some_user_name')


@app.route("/json", methods=['POST'])
def read_json():
    return jsonify({"greeting": "Hello, " + request.json['name']})