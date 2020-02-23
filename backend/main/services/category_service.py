from flask_restful import abort
from backend.main.API_Exceptions import *

from backend.main.models.category import Category


def get_categories():
    response = Category.query.all()
    return response


def post_category(data):
    data = data['category']

    if data.get('name') is None:
        response_object = {
            'status': 'error',
            'message': 'name is required'
        }
        return response_object, 422

    category = create_category_from_json(data)
    inserted_category = category.insert()
    return inserted_category.format(), 201


# Helper methods
def create_category_from_json(json_data):
       return Category(name=json_data.get('name'),
                    description= json_data.get('description'),
                    slug=json_data.get('slug'))
