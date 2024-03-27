
# Local Setup
## Prerequisites
- (Docker Desktop)[https://www.docker.com/products/docker-desktop/] is installed. 
- Python

## Steps
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
## Connecting to Docker
Ensure Docker Desktop is running.

### Windows
bat files have been created to make terminal commands a bit easier. 
In _command prompt_ run `build.bat` to build the image after adding new dependencies
Use `run.bat` to mount the folder and use a volume

### Mac / Linux
bat files can be converted to bash scripts. The path in run.bat may require a different way to refer to the current directory. Instructions to be updated once I can confirm what's required. 

## Database
API uses Flask Migrate. When making table changes, we need to create and commit the migration files.
Create the migration file to make required DB changes
`flask db migrate`

To actually run the changes in the DB. __NOTE__: Command will use the environment variable and run these changes on the remote DB if configured. Docker setup commands should take care of this for deployments. Manually run fo
`flask db upgrade`

