# mortygage_calculator

<p align="center">
  <img src="https://raw.githubusercontent.com/LucasSRocha/mortygage_calculator/main/morty.gif" alt="morty oh gee" >
</p>

## Objective of this repo
Oh geez, how to write this?
The objective here is to demonstrate a mortgage calculator api that follows the guidelines of the Province of British Columbia.

## Environments
[dev](https://mortygagecalculator1-8rochalucas.b4a.run/docs)

## How to use
### Requirements
- [python](https://www.python.org/downloads/)
- [docker](https://www.docker.com/get-started/)

Optional:
- [pyenv](https://github.com/pyenv/pyenv)


### Local
to run this repository locally you have two options.
1. running it through a docker container.
To do so you can simply execute:
```shell
$ docker-compose up --build
```
This will build the image and run the container making the server available at `localhost:8000`.


2. running the server locally
To do so you need to do a couple steps:  
    2.1 create a virtual environment to isolate the project.  
    2.2 install the dependencies.  
    2.3 run the start command.  

```shell
$ python -m virtualenv venv
$ source .venv/bin/activate
$ make dev-dependencies 
$ make run-local
```
This will start the server locally and make it available at `localhost:8000`


### Testing
To execute tests you can use the `make test-coverage` when inside the local virtual environment.

## Thought process/ Ideas
The objective of this project was to propose an open API endpoint specifically designed for calculating mortgage payments, as part of a larger project that handles other aspects related to loans. Given the tight two-day deadline for this project, I decided to build the API using fastAPI. Its solid and speedy framework, coupled with its easy-to-use documentation and validation features, made it the ideal choice for rapidly expanding the domain of our service.

The vision I had for this project was to construct both the backend and frontend, along with a Backend for Frontend (BFF) interface. The BFF would allow us to communicate with the primary backend without exposing it, and it would also serve as a location for any necessary data transformation.

