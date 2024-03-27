# circus-movement-rest-api
API for Circus movement information and routine builder app

Live for testing at: https://circus-routine-rest-api.onrender.com

# Purpose
To connect moves to different types of aerial apparatuses. Each apparatus will also have various types that are important distinctions. 
Gives flexibility to add apparatuses how the user wants. The aerial circus world is taught in so many different ways, and there are multiples ways to refer to both apparatuses and moves. (Example: Tissu vs Silks, and any number of studio grown titles for movements)
Eventually app should have a default so new to circus users can jump in. V1 will be completely custom. 

## Endpoint Information
https://circus-routine-rest-api.onrender.com/swagger-ui


### Apparatuses
These are the pieces of equipment that aerial acrobatics perform their moves (or tricks) on. 

### Moves
A movement or trick that can be done on a corresponding apparatus. How these are executed can be effect by the type. 

## Thirdparty Sources
Services used for creation of code thus far.
elephantsql.com - created Postgres DB for development and production
render.com - where live API is hosted

## Later Development
Incorporate routines to allow users to build performances by selecting an apparatus and browsing related moves. 

### Endpoint 'Type' - Not Yet Implemented
A piece of info to categorize the apparatuses. They are considered Soft Apparatuses (Ex. Silks, Rope, Straps, ect) or Hard Apparatuses (Ex. Trapeze, Lyra, Cubes).
And to categories further, some of these equipment can be rigged using a single point, or double point, or other configurations that make it a distinctly different experience with different moves available. 
