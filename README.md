# mortygage_calculator

<p align="center">
  <img src="https://raw.githubusercontent.com/LucasSRocha/mortygage_calculator/main/morty.gif" alt="morty oh gee" >
</p>

## Objective of this repo
Oh geez, how to write this?
The objective here is to demonstrate a mortgage calculator api that follows the guidelines of the British Columbia Province.

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
    2.1 create a virtual environment to isolate the project
    2.2 install the dependencies
    2.3 run the start command

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
The objective of this project was to provide an idea of an open api endpoint dedicated to calculate mortgage payments in a project that handles more things related to loans.
Considering the two days to deliver constraint I've decided to built the API with fastAPI because it provides solid and fast (pun not intended) base to expand the domain with easy documentation and validation for our service.

Talking about the whole project the vision would be to construct this backend plus the frontend with a bff(backend for frontend) to provide an interface in which we can comunicate with the primary backend without exposing it and having a place in which we can do any data transformation if necessary.

