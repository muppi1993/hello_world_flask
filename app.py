from flask import Flask
from flask import request
from flask import jsonify
from flask_expects_json import expects_json
import datetime

from rq_function import add, count_lines, poppunk_assign
from redis import Redis
from rq import Queue

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

schema2 = {
  "type": "object",
  "properties": {
    "path": { "type": "string" }
  },
  "required": ["path"]
}

#homepage
@app.route('/')
def hello_world():
    return 'Hello, World!'
    
#take json input (according to schema) and return json
@app.route("/json", methods=['POST'])
@expects_json(schema)
def read_json():
    timestamp = datetime.datetime.now().isoformat()
    if 'lastname' in request.json:
        return jsonify({"greeting": "Hello, " + request.json['firstname']+" "+request.json['lastname'], "timestamp":timestamp})
    else:
        return jsonify({"greeting": "Hello, " + request.json['firstname'], "timestamp":timestamp})
    #curl -H "Content-Type: application/json" --data '{"firstname": "Marie","lastname":"Gronemeyer","age":29}' http://127.0.0.1:5000/json

#run some jobs in a rq
@app.route("/rq")
def try_rq():
  q = Queue(connection=Redis())
  result = q.enqueue(add, 5,5)
  result2 = q.enqueue(count_lines, 'poppunk/input_data/qfile.txt')
  return "All jobs submitted\n"
  #curl http://127.0.0.1:5000/rq

#run poppunk in a rq
@app.route("/poppunk", methods=['POST'])
@expects_json(schema2)
def try_poppunk():
  q = Queue(connection=Redis())
  result = q.enqueue(poppunk_assign,request.json['path'])
  return "All jobs submitted\n"
  #curl -H "Content-Type: application/json" --data '{"path":"/home/mmg220/Documents/poppunk"}' http://127.0.0.1:5000/poppunk