from flask import Flask, jsonify
from flask_cors import CORS
from backend.db_config import setup_db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    print('App running...')
    setup_db(app)
    print('setup_db EXECUTED...')
    CORS(app)
    return app


APP = create_app()

@APP.route('/', methods=(['GET']))
def index():
    print('index called')
    return jsonify({'value': 'hello'})


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
