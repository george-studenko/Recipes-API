from flask_restplus import Resource
from flask import request
from backend.main.services.category_service import *
from backend.main.dtos import CategoryDTO
from backend.main.API_Exceptions import *


api = CategoryDTO.CategoryDTO.api
dto = CategoryDTO.CategoryDTO.category


@api.route('/')
class CategoryList(Resource):
    @api.doc('Get categories')
    @api.marshal_with(dto)
    def get(self):
        return get_categories(), 200


    @api.doc('Post a new category')
    @api.response(201, 'Category successfully created.')
    def post(self):
        data = request.get_json()
        response, status_code = post_category(data)
        if status_code is not 201:
            abort(status_code)

        return response, status_code


@api.route('/<id>')
@api.param('id', 'The Category id')
@api.response(404, 'User not found.')
class Category(Resource):
    @api.doc('get a singe category')
    @api.marshal_with(dto)
    def get(self, id):
        """get a category given its id"""
        category = get_category_by_id(id)
        if not category:
            api.abort(404)
        return category


@api.errorhandler(UnprocessableError)
def unprocessable_entity(self, exception):
    return {
        'error': exception.error,
        'success': False
    }, 422



