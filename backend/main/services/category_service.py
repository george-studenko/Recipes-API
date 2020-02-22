from backend.main.models.category import Category


def get_categories():
    response = Category.query.all()
    return response


def post_category(data):
    category = create_category_from_json(data['category'])
    inserted_category = category.insert()
    return inserted_category


# Helper methods
def create_category_from_json(json_data):
    return Category(name=json_data.get('name'),
                    description= json_data.get('description'),
                    slug=json_data.get('slug')
                    )