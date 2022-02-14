from flask import Flask
from flask import request
from flask import jsonify
from flask_expects_json import expects_json
import datetime

app = Flask(__name__)

schema = {
  "type": "object",
  "properties": {
    "firstname": { "type": "string" },
    "lastname": { "type": "string" },
    "age": {"type": "number"}
  },
  "required": ["firstname"]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route("/json", methods=['POST'])
@expects_json(schema)
def read_json():
    timestamp = datetime.datetime.now().isoformat()
    if 'lastname' in request.json:
        return jsonify({"greeting": "Hello, " + request.json['firstname']+" "+request.json['lastname'], "timestamp":timestamp})
    else:
        return jsonify({"greeting": "Hello, " + request.json['firstname'], "timestamp":timestamp})