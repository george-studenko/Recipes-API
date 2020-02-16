from backend.main.models.category import Category


def get_categories():
    response = Category.query.all()
    return response, 200


def post_category(name, description, slug):
    category = Category(name,description,slug)
    category.insert()
