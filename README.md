# Recipes API
This is a flask restful API for managing recipes.

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

## API Setup
When running for the first time it will be necessary to follow these steps:
1. Create the postgres db with ```createdb recipesDB```
1. Apply the database migrations with ```python manage.py db upgrade```

## Running the API
1. To run the API execute ```python manage.py run```

## Test Setup
When running the api tests for the first time it will be necessary to follow these steps:
1. Create the postgres db with ```createdb recipesTestDB```
1. Apply the database migrations with ```python manage.py db upgrade```

## Running the API Test
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
There are 4 resources in this endpoint:
1. ```/health```: as described above. Allowed verbs are: ```GET```
1. ```user```: To post users, required to post a recipe. Allowed verbs are: ```POST```
1. ```category```: To manage recipe categories. Allowed verbs are: ```GET```, ```POST```, ```PATCH```, ```DELETE```
1. ```recipe```: To manage recipes. Allowed verbs are: ```GET```, ```POST```, ```PATCH```, ```DELETE```
## TO DO
1. Implement scriptline to automate database creation.