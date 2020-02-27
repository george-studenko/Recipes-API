# Recipes API
This is a flask restful API for managing recipes.

## Motivation
The motivation behind this API is to learn and develop my skills programming with python at the same time trying to 
create a well structure project with differentiated layers. 

For a better architecture I've also included a 2nd branch which follows a more elaborated and maintainable architecture:
```https://github.com/george-studenko/fs.capstone/tree/apiWithFlaskRestplus```  while it is not fully finished and 
implemented it already contains the main components of the application.

I also wanted to practice deploying apps to ```heroku```, integrating a third party authentication service as 
```auth0``` and write some good unit tests.

This API can be used as a starting point to develop other APIs.

The API is hosted in heroku with the following url:  
```https://recipes-pro.herokuapp.com/health```

## API Requirements
The required packages are:
```
alembic==1.4.0
Click==7.0
ecdsa==0.15
Flask==1.1.1
Flask-Cors==3.0.8
Flask-Migrate==2.5.2
Flask-Script==2.0.6
Flask-SQLAlchemy==2.4.1
Flask-Testing==0.7.1
gunicorn==20.0.4
itsdangerous==1.1.0
Jinja2==2.11.1
Mako==1.1.1
MarkupSafe==1.1.1
psycopg2==2.8.4
pyasn1==0.4.8
python-dateutil==2.8.1
python-editor==1.0.4
python-jose==3.1.0
rsa==4.0
six==1.14.0
SQLAlchemy==1.3.13
Werkzeug==0.16.1
```
These requirements are listed in ```requirements.txt```   

Requirements can be easily installed by executing:  
```pip install -r requirements.txt```

## Local API Setup
When running for the first time it will be necessary to follow these steps:
1. Create the postgres db with ```createdb recipesDB```
1. Apply the database migrations with ```python manage.py db upgrade```
1. Open ```api/controllers.py``` find the ```create_app``` method and replace ```environment='heroku'``` with 
```environment='dev'```

## Running the API locally
1. To run the API execute ```python manage.py run```

## Local Test Setup
When running the api tests for the first time it will be necessary to follow these steps:
1. Create the postgres db with ```createdb recipesTestDB```
1. Apply the database migrations with ```python manage.py db upgrade```
1. Open ```tests/base_test_case.py```, find the ```create_app``` method and replace  ```app.config.from_object('infraestructure.config.Heroku_Test_Config')```
 for ```app.config.from_object('infraestructure.config.Test_Config')``` 

## Running the local API Tests
1. To run the API execute ```python manage.py test```

## Health Check
I have created an open endpoint to check the API health, no need for authentication to access this endpoint
To check if the API is running successfully in the local server to the following endpoint:   
```http://localhost:5000/health/```

To test the published API health at Heroku open:   
```https://recipes-pro.herokuapp.com/health``` 
  
The ```/health``` enfpoint should return a ```200``` response with the following content:  
```
{
    "healthy": true,
    "message": "Service is up and running"
}
```

## API Endpoints
1. ```/health```: as described above. Allowed verbs are: ```GET```
1. ```/user```: To post users, required to post a recipe. Allowed verbs are: ```POST```
1. ```/category```: To get the list of categories and post a category. Allowed verbs are: ```GET```, ```POST```
1. ```/category/<id>```: To manage recipe categories. Allowed verbs are: ```GET```, ```PATCH```, ```DELETE```
1. ```/recipe```: To get a list of recipes and post recipes. Allowed verbs are: ```GET```, ```POST```
1. ```/recipe/<id>```: To manage recipes. Allowed verbs are: ```GET```, ```PATCH```, ```DELETE```


## User Roles
Authentication is managed with ```Auth0```

Two roles exist:
1. ```cook```: this role is a read only role, users with this role are allowed to execute the ```GET``` 
verb in all endpoints
1. ```chef```: this role is a read and write role, allowing full access to all endpoints, ```chefs``` 
are allowed to ```GET```,```POST```, ```PATCH``` and ```DELETE``` recipes and categories as well as ```POST``` users.

## Testing the API

To call the API protected endpoints a JWT token must be included as the Bearer token, below I'm providing a temporal 
token for each role

```cook``` bearer token:  

```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1qZ3pRemMyTXpORE1rRkdNRGRDUWpVeVFVUkZSa0UxTTBJek5EZEdSRFZDUWtKRk1qRkVRZyJ9.eyJpc3MiOiJodHRwczovL2duc2QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTA0NjQ2Nzc4MTc2NDQ4MzE3OTIyIiwiYXVkIjpbIlJlY2lwZXNBUEkiLCJodHRwczovL2duc2QuZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4Mjg0Mjg3NCwiZXhwIjoxNTgyOTI5MjczLCJhenAiOiJPOXo0RkJ5U1dQNzJtdGNnejBmNDJRNUZGZlFoRTJzNyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Y2F0ZWdvcnkiLCJnZXQ6cmVjaXBlIl19.ChjQEG-vGHvkFd0NUayC2QhK7JkD0PEZOFacCsz3l0vCSLvmWvCi9NPPT32yqTAOK9ji0i4RxD8G6zG7dDgfP7vN10IB3U1Z9Cm3Lx4L2c0xOoxmQhKqEgkt2UfdHLNz3BwNOZVxKlrE-wvYiXW4vkIjUHFbwUggKwD79TM3lQ7J2Ixc6KYYdgh43qWrap2H6w2iiQ0HkcbRm1yZ61yZ8V_q68RPpVZQJovbD1-F9jugE0DYyiPzZ4aLuYqKvXvbdYXJSBEThi9CDxyVa-H1nZFM-gJ-yIhDUqCW4NiHIRQqVC7GeOgIePXf1aNDTxs-FNidYH3PfSImFCj_9TsnhA```


```chef``` bearer token:  

```eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1qZ3pRemMyTXpORE1rRkdNRGRDUWpVeVFVUkZSa0UxTTBJek5EZEdSRFZDUWtKRk1qRkVRZyJ9.eyJpc3MiOiJodHRwczovL2duc2QuZXUuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEzMjE4MDA0MjE0OTE4ODk1ODU3IiwiYXVkIjpbIlJlY2lwZXNBUEkiLCJodHRwczovL2duc2QuZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4MjgzODQ3NywiZXhwIjoxNTgyOTI0ODc2LCJhenAiOiJPOXo0RkJ5U1dQNzJtdGNnejBmNDJRNUZGZlFoRTJzNyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Y2F0ZWdvcnkiLCJkZWxldGU6cmVjaXBlIiwiZ2V0OmNhdGVnb3J5IiwiZ2V0OnJlY2lwZSIsInBhdGNoOmNhdGVnb3J5IiwicGF0Y2g6cmVjaXBlIiwicG9zdDpjYXRlZ29yeSIsInBvc3Q6cmVjaXBlIiwicG9zdDp1c2VyIl19.OVZy5z_0josOoIG-cDB1CSpSPpxC2An3KCvkouA99HzaUdi_C_EfK4H-mMCb2N5tnK1aGScWRlf5Bxa2yDC34YbgfalwCs72H8t4VeThEMi7LILfJMUiVckiMIGYqYpsIefZ_u1KY_2NuQVnewDlxMJceXL9z2Cx-UHr4OthCXpbSkRKbbgzLfhWQ_lZYcO45qQn3HDds3JN9rr_RBgyn-VYoSfC3PCIJgXfqH-STpBh-JI4U0zskAh4vJFcdYpCo-Cpr0jpSFHSevrRlWEVZrCNROSqgLekRc7lj1wW7rIOlUEEL6mI5ugOlrTgz96zFmS38-fOb1kqHw5oMiqCaw```
## TO DO's
1. Mock out the authentication to: speed up unit tests and make it possible to run them independently of the auth0 service
1. Implement scriptline to automate database creation.