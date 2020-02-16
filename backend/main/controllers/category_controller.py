from flask_restplus import Resource
from backend.main.services.category_service import get_categories
from backend.main.dtos import CategoryDTO


api = CategoryDTO.CategoryDTO.api
dto = CategoryDTO.CategoryDTO.category


@api.route('/')
class Category(Resource):
    @api.doc('Get categories')
    @api.marshal_with(dto, envelope='categories')
    def get(self):
        return get_categories()
