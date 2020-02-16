from flask import Flask
from flask_cors import CORS
from .config import environments
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def setup_db(app, environment):
    app.config.from_object(environments[environment])
    db.app = app
    print('db.app: ', environment)
    db.init_app(app)


def create_app(environment='dev'):
    # create and configure the app
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    setup_db(app, environment)
    CORS(app)
    return app


