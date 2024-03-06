# circus-movement-rest-api
API for Circus movement information and routine builder app


# Purpose
To connect moves to different types of aerial apparatuses. Each apparatus will also have various types that are important distinctions. 
Gives flexibility to add apparatuses how the user wants. The aerial circus world is taught in so many different ways, and there are multiples ways to refer to both apparatuses and moves. (Example: Tissu vs Silks, and any number of studio grown titles for movements)
Eventually app should have a default so new to circus users can jump in. V1 will be completely custom. 

## Key Information involved:
### Apparatuses
These are the pieces of equipment that aerial acrobatics perform their moves (or tricks) on. 

### Type
A piece of info to categorize the apparatuses. They are considered Soft Apparatuses (Ex. Silks, Rope, Straps, ect) or Hard Apparatuses (Ex. Trapeze, Lyra, Cubes).
And to categories further, some of these equipment can be rigged using a single point, or double point, or other configurations that make it a distinctly different experience with different moves available. 

### Moves
A movement or trick that can be done on a corresponding apparatus. How these are executed can be effect by the type. 

## Later Development
Incorporate routines to allow users to build performances by selecting an apparatus and browsing related moves. 


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