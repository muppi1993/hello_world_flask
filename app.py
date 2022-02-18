from flask import Flask, request, jsonify
from flask_expects_json import expects_json
import datetime
from redis import Redis
from rq import Queue
from rq.job import Job

from rq_function import add, count_lines, poppunk_assign


app = Flask(__name__)
redis=Redis()


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
  q = Queue(connection=redis)
  result = q.enqueue(add, 5,5)
  result2 = q.enqueue(count_lines, 'poppunk/input_data/qfile.txt')
  print(result.id)
  return jsonify([{"id": result.id, "status":"curl http://127.0.0.1:5000/status/"+result.id,"result": "curl http://127.0.0.1:5000/result/"+result.id},
  {"id": result2.id, "status":"curl http://127.0.0.1:5000/status/"+result2.id,"result": "curl http://127.0.0.1:5000/result/"+result2.id}])
  #curl http://127.0.0.1:5000/rq


#run poppunk in a rq
@app.route("/poppunk", methods=['POST'])
@expects_json(schema2)
def try_poppunk():
  q = Queue(connection=redis)
  result = q.enqueue(poppunk_assign,request.json['path'])
  return jsonify({"id": result.id, "status":"http://127.0.0.1:5000/status/"+result.id,"result": "http://127.0.0.1:5000/result/"+result.id})
  #curl -H "Content-Type: application/json" --data '{"path":"/home/mmg220/Documents/flask-tutorial/poppunk"}' http://127.0.0.1:5000/poppunk


#get job status
@app.route("/status/<id>")
def get_status(id):
  job = Job.fetch(id, connection=redis)
  if job.get_status() =="finished":
    return jsonify ({"id": id, "status":job.get_status(), "result":job.result, "result location": "curl http://127.0.0.1:5000/result/"+id})
  else:
    return jsonify ({"id": id, "status":job.get_status()})


#get job result
@app.route("/result/<id>")
def get_result(id):
  job = Job.fetch(id, connection=redis)
  if job.result==None:
    return "Result not ready yet\n"
  else:
    return str(job.result)+"\n"
