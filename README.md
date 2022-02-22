# hello_world_flask
Project to learn and try out Flask and rq

Clone the repo on your machine. 

You need 
- [Pyton3](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/engine/install/)
- [PopPUNK](https://github.com/johnlees/PopPUNK)

installed, as well as the dependencies in requirements.txt. These can be installed with with `pip install -r requirements.txt`

Go to the project folder and
1. run `./scripts/run` to start the flask app, the Redis server and a worker.
2. In a second terminal, you can query the different Routes:
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
  - At /status/JobID and /result/JobID you can retrieve information about the submitted jobs. The respective JobIDs will be provided when jobs are submitted.
    ```
    curl http://127.0.0.1:5000/status/JobID
    curl http://127.0.0.1:5000/result/JobID
    ```
  - At /version the version number of this application is returned. To run this, you must first package this project with `python -m build`, then install it with `pip install .` Once you've done this, you can query:
    ```
    curl http://127.0.0.1:5000/version
    ```
3. At the end, stop the flask app, Redis server and worker in the first terminal with ctrl+c.
