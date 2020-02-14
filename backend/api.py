from backend.app import APP
from flask import Flask, request, abort, jsonify


@APP.route('/i', methods=(['GET']))
def index():
    print('index called')
    return jsonify({'value': 'hello WOOOORLD'})
