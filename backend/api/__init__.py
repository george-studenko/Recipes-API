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

@app.errorhandler(422)
def unprocessable_entity(error):
    print(error)
    return jsonify(
        {
        'error': str(error),
        'success': False
        }
        ), 422

@app.errorhandler(404)
def not_found(error):
    print(error)
    return jsonify(
        {
        'error': str(error),
        'success': False
        }
        ), 404

#
#
# @api.route('/<id>')
# @api.param('id', 'The Category id')
# @api.response(404, 'User not found.')
# class Category(Resource):
# @api.doc('get a category by id')
# @api.marshal_with(dto)
# def get(self, id):
#     """Get a category given its id"""
#     category = service.get_category_by_id(id)
#     if not category:
#         api.abort(404)
#     return category
#
# @api.doc('update a category by id')
# def patch(self, id):
#     '''To partially update a category'''
#     category = request.get_json()
#     response = service.patch(id, category)
#     return response
#
# @api.doc('delete a category by id')
# def delete(self, id):
#     '''Delete a category by id'''
#     response = service.delete_category_by_id(id)
#     if response is None:
#         abort(404)
#     return response, 200
#
# # TODO: errorhandler not working
# @api.errorhandler(UnprocessableError)
# def unprocessable_entity(exception):
#     return {
#         'error': exception.error,
#         'success': False
#     }, 422

 # Helper methods
def create_category_from_json(json_data):
       return Category(name=json_data.get('name'),
                       description= json_data.get('description'),
                       slug=json_data.get('slug'))

if __name__ == '__main__':
    app.run()
