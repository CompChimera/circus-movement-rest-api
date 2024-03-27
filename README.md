# circus-movement-rest-api
API for Circus movement information and routine builder app

Live for testing at: https://circus-routine-rest-api.onrender.com

# Purpose
To connect moves to different types of aerial apparatuses. Each apparatus will also have various types that are important distinctions. 
Gives flexibility to add apparatuses how the user wants. The aerial circus world is taught in so many different ways, and there are multiples ways to refer to both apparatuses and moves. (Example: Tissu vs Silks, and any number of studio grown titles for movements)
Eventually app should have a default so new to circus users can jump in. V1 will be completely custom. 

## Key Information involved:

## Endpoint Information
https://circus-routine-rest-api.onrender.com/swagger-ui


### Apparatuses
These are the pieces of equipment that aerial acrobatics perform their moves (or tricks) on. 

### Moves
A movement or trick that can be done on a corresponding apparatus. How these are executed can be effect by the type. 

## Later Development
Incorporate routines to allow users to build performances by selecting an apparatus and browsing related moves. 

### Type - Not Yet Implemented
A piece of info to categorize the apparatuses. They are considered Soft Apparatuses (Ex. Silks, Rope, Straps, ect) or Hard Apparatuses (Ex. Trapeze, Lyra, Cubes).
And to categories further, some of these equipment can be rigged using a single point, or double point, or other configurations that make it a distinctly different experience with different moves available. 

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
Ensure (Docker Desktop)[https://www.docker.com/products/docker-desktop/] is installed. 

### Windows
bat files have been created to make terminal commands a bit easier. 
In _command prompt_ run `build.bat` to build the image after adding new dependencies
Use `run.bat` to mount the folder and use a volume


## Local DB
Flask Migrate
Create the migration file to make required DB changes
`flask db migrate`

To actually run the changes in the DB 
`flask db upgrade`

## Thirdparty Sources
elephantsql.com - created Postgres DB for development and production
render.com - where live API is hosted
