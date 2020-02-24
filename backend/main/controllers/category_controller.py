from flask_restplus import Resource
from flask import request
from backend.main.services.category_service import *
from backend.main.dtos import CategoryDTO
from backend.main.API_Exceptions import *

api = CategoryDTO.CategoryDTO.api
dto = CategoryDTO.CategoryDTO.category
service = Category_Service()

@api.route('/')
class CategoryList(Resource):
    @api.doc('Get categories')
    @api.marshal_with(dto)
    def get(self):
        '''Get the list of all cagegories'''
        return service.get_categories(), 200


    @api.doc('Post a new category')
    @api.response(201, 'Category successfully created.')
    def post(self):
        '''Creates a new category'''
        data = request.get_json()
        response, status_code = service.post(data)
        if status_code is not 201:
            abort(status_code)

        return response, status_code


@api.route('/<id>')
@api.param('id', 'The Category id')
@api.response(404, 'User not found.')
class Category(Resource):
    @api.doc('get a category by id')
    @api.marshal_with(dto)
    def get(self, id):
        """Get a category given its id"""
        category = service.get_category_by_id(id)
        if not category:
            api.abort(404)
        return category

    @api.doc('update a category by id')
    def patch(self, id):
        '''To partially update a category'''
        category = request.get_json()
        response = service.patch(id, category)
        return response

    @api.doc('delete a category by id')
    def delete(self, id):
        '''Delete a category by id'''
        response = service.delete_category_by_id(id)
        if response is None:
            abort(404)
        return response, 200

# TODO: errorhandler not working
@api.errorhandler(UnprocessableError)
def unprocessable_entity(exception):
    return {
        'error': exception.error,
        'success': False
    }, 422



