from flask import jsonify, request, abort
from models import *
from flask import Flask
from flask_cors import CORS
from database import db
from .config import environments


def setup_db(app, environment):
    app.config.from_object(environments[environment])
    db.app = app
    db.init_app(app)


def create_app(environment='dev'):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    setup_db(app, environment)
    CORS(app)
    return app

app = create_app()

@app.route('/health')
def check_health():
    response = jsonify({'healthy': True,
                        'message': 'Service is up and running'}
                       )
    return response


@app.route('/category', methods=['GET'])
def get_categories():
    '''Get the list of all cagegories'''
    categories = Category.query.all()
    if categories is None:
        abort(404,'No categories found')
    formatted_categories = [category.format() for category in categories]
    return jsonify({
        'success': True,
        'categories': formatted_categories
    }), 200


@app.route('/category/<id>', methods=['GET'])
def get_category(id):
    """Get a category given its id"""
    category = Category.query.get(id)
    if not category:
        abort(404)

    response = jsonify({
        'success': True,
        'category': category.format()
    })
    return response


@app.route('/category', methods=['POST'])
def post_category():
    '''Creates a new category'''
    json = request.get_json()

    data = json['category']

    if data.get('name') is None:
        abort(422,'Name is required')
    category = create_category_from_json(data)
    inserted_category = category.insert()

    response = jsonify({
        'success': True,
        'category': inserted_category.format()
    })

    return response, 201


@app.route('/category/<id>', methods=['DELETE'])
def delete(id):
    '''Delete a category by id'''
    category = Category.query.get(id)
    if category is None:
        abort(404)

    category.delete()
    response = jsonify( {
        'success': True
    })
    return response, 200


@app.route('/category/<id>', methods=['PATCH'])
def patch(id):
    original_category =  Category.query.get(id)
    if original_category is None:
        abort(404,'category does not exist')

    json_category = request.get_json()
    category = create_category_from_json(json_category['category'])

    if category.description is not None:
        original_category.description = category.description

    if category.name is not None:
        original_category.name = category.name

    if category.slug is not None:
        original_category.slug = category.slug

    original_category.update()

    response = jsonify({
        'success': True,
        'category': original_category.format()
    })
    return response, 200


@app.errorhandler(422)
def unprocessable_entity(error):
    return jsonify(
        {
        'error': str(error),
        'success': False
        }
        ), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify(
        {
        'error': str(error),
        'success': False
        }
        ), 404

 # Helper methods
def create_category_from_json(json_data):
       return Category(name=json_data.get('name'),
                       description= json_data.get('description'),
                       slug=json_data.get('slug'))

if __name__ == '__main__':
    app.run()
