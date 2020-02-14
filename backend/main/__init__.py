from flask import Flask
from flask_cors import CORS
from main.config import environments
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def setup_db(app, environment):
    app.config.from_object(environments[environment])
    db.app = app
    print('db.app: ', app)
    db.init_app(app)
    print('db.init EXECUTED')


def create_app(environment='dev'):
    # create and configure the app
    app = Flask(__name__)
    print('App running...')
    setup_db(app, environment)
    print('setup_db EXECUTED...')
    CORS(app)
    return app


# APP = create_app()
#
# @APP.route('/', methods=(['GET']))
# def index():
#     print('index called')
#     return jsonify({'value': 'hello'})



