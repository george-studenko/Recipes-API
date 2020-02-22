from flask_restplus import Resource
from flask import request
from backend.main.services.category_service import *
from backend.main.dtos import CategoryDTO


api = CategoryDTO.CategoryDTO.api
dto = CategoryDTO.CategoryDTO.category


@api.route('/')
class Category(Resource):
    @api.doc('Get categories')
    @api.marshal_with(dto, envelope='categories')
    def get(self):
        return get_categories(), 200

    @api.doc('Post a new category')
    @api.response(201, 'Category successfully created.')
    @api.marshal_with(dto, envelope='category')
    def post(self):
        data = request.get_json()
        inserted_category = post_category(data)
        return inserted_category, 201

