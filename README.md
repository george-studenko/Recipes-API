# Recipes API
This is a flask restful API for managing recipes

## API Components
1. flask_restplus: to help with the API architecture and generate Swagger documentation
1. flask_script: to manage all commands related to the API such as run the app, execute tests and manage db migrations
1. SQLAlchemy: as the API ORM  
1. Blueprints: for a better organization of the API components
1. Postman Collection: a collection of calls to manually test the API endpoints

## API Setup
When running for the first time it will be necessary to follow these steps:
1. Create the postgres db with ```createdb recipesDB```
1. Apply the database migrations with ```python manage.py db upgrade```

## Running the API
1. To run the API execute ```python manage.py run```

## Health Check
To check if the API is running successfully go to the following endpoint:   
```http://localhost:5000/health/```   
  
It should return a ```200``` response with the following content:  
```
{
    "healthy": true,
    "message": "Service is up and running"
}
```
