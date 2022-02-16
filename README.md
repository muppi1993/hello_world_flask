# hello_world_flask
Project to learn and try out Flask and rq

Clone the repo on your machine. 

You need 
- [Flask](https://flask.palletsprojects.com/en/1.0.x/installation/#installation)
- [Redis](https://redis.io/download)
- [rq](https://python-rq.org/)
- [PopPUNK](https://github.com/johnlees/PopPUNK)

installed. 

1. Start the Redis server with `src/redis-server` from the redis installation folder
2. In a second terminal, go to the project folder andd run the flask app with `flask run`
3. In a third terminal, start a worker inside the project folder with `rqworker`
3. In a fourth terminal, you can query the different Routes:
  - At /json you can submit data in json format and receive a json with a greeting and timestamp back
  
  Run 
  ```
  curl -H "Content-Type: application/json" --data '{"firstname": "John","lastname":"Doe","age":99}' http://127.0.0.1:5000/json
  ```
  - At /rq two simple jobs are submittet to the redis queue ( addition of 5+5 and counting of lines in a file)
  
  Run
  ```
  curl http://127.0.0.1:5000/rq
  ```
  - At /poppunk you can run a cluster assignment using poppunk. 
  To do this, you must first downlod the GPS S. pneumoniae full database from https://poppunk.net/pages/databases.html and unpack it into the poppunk folder.
  
  Run the following command with adjusted path:
  ```
  curl -H "Content-Type: application/json" --data '{"path":"/path/to/flask-tutorial/poppunk"}' http://127.0.0.1:5000/poppunk
  ```
  
 The results from the rq can be viewed in the third terminal with the rqworker.
