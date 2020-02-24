from flask_restful import abort
from backend.main.API_Exceptions import *

from backend.main.models.category import Category


class Category_Service():

    def get_categories(self):
        response = Category.query.all()
        return response

    def get_category_by_id(self, id):
        response = Category.query.get(id)
        return response

    def delete_category_by_id(self, id):
        category = Category.query.get(id)
        response = None
        if category is not None:
            category.delete()
            response = {
                'success': True
            }
        return response

    def post(self, data):
        data = data['category']

        if data.get('name') is None:
            response_object = {
                'status': 'error',
                'message': 'name is required'
            }
            return response_object, 422

        category = self.create_category_from_json(data)
        inserted_category = category.insert()
        return inserted_category.format(), 201

    def patch(self, id, json_category):
        original_category = self.get_category_by_id(id)
        if original_category is None:
            response_object = {
                'status': 'error',
                'message': 'category does not exist'
            }
            return response_object, 404

        category = self.create_category_from_json(json_category['category'])
        response = None

        if original_category is not None:
            if category.description is not None:
                original_category.description = category.description

            if category.name is not None:
                original_category.name = category.name

            if category.slug is not None:
                original_category.slug = category.slug

            original_category.update()

            response = {
                'success': True
            }

        return response

    # Helper methods
    def create_category_from_json(self, json_data):
           return Category(name=json_data.get('name'),
                           description= json_data.get('description'),
                           slug=json_data.get('slug'))
