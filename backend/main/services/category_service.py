from backend.main.models import category
from backend.main import db

def get_categories():
    response = category.Category.query.all()
    return response, 200
