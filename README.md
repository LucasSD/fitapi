# Introduction

The aim of this project is to create a simple API using Flask and Connexion. Only GET methods have been included. 

## Technologies

Python, Flask, Connexion, SQLAlchemy, Marshmallow

## Getting Started

Please follow the instructions below to run this application. 

1 - download this repo as a zip file and unzip it to your working directory.  
2 - install Python 3.9 or later

## (Optional) Create and use a virtual environment:
## https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment
```python -m venv env```

```source env/bin/activate```

## Install dependencies:
## https://pip.pypa.io/en/stable/user_guide/#requirements-files
```pip install -r requirements.txt```

## Run my tests (all should pass):
```pytest```

## Optional: run Coverage (using batch file) to receive a test coverage report in stdout
```cvrg.bat```

## Start the development server:
```python server.py```

After these commands, you should be able to see the Swagger UI at http://localhost:5000/api/ui. All URL endpoints stated in the UI are functional. An unfinished Single Page application is visible at http://localhost:5000.

## Project Status

Still being developed. 
###### To do:

- consider adding functionality for all HTTP verbs. 
- improve test suite
- finish Single Page Application
- extend with additional models
