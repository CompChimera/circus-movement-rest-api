# circus-movement-rest-api
API for Circus movement information and routine builder app

# Setup
First we setup the virutal environment
`python3.12 -m venv .venv`

In VSCode, select interpreter
`Ctrl + shift + p` and search for Python Interpreter. Select the one in the project.

Once you’ve created a virtual environment, you may activate it.

On Windows, run:
`.venv\Scripts\activate`

On Unix or MacOS, run:
`source tutorial-env/bin/activate`

Install the dependencies
`pip install -r requirements.txt`

Then we're ready to connect to Docker!


## Using docker locally
Ensure Docker Desktop is installed. 

We also need to run these two commands each time we add new dependencies to install
To setup the container `docker build -t circus-api .`


To mount the folder on Windows and use a volume:
`docker run -dp 5000:5000 -w /app -v %cd%:/app circus-api `