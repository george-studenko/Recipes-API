import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from flask import jsonify, request, abort
from domain.models import *
from service.health_service import Health_Service
from flask import Flask
from flask_cors import CORS
from infraestructure.database import db
from infraestructure.config import environments
from .authentication.auth import requires_auth, AuthError


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

health_service = Health_Service()

# region Health Controller
@app.route('/health')
def check_health():
    response = health_service.check_health()
    return response
# endregion

# region User Controller
@app.route('/user', methods=['POST'])
@requires_auth(permission='post:user')
def post_user():
    '''Creates a new user'''
    json = request.get_json()

    data = json['user']

    if data.get('username') is None:
        abort(422,'username is required')
    user = create_user_from_json(data)
    inserted_user = user.insert()

    response = jsonify({
        'success': True,
        'recipe': inserted_user.format()
    })

    return response, 201

# endregion


# region Recipe Controller
@app.route('/recipe', methods=['GET'])
@requires_auth(permission='get:recipe')
def get_recipes():
    '''Get the list of all recipes'''
    recipes = Recipe.query.all()
    if len(recipes) is 0:
        abort(404,'No recipes found')
    formatted_recipes = [recipe.format() for recipe in recipes]
    return jsonify({
        'success': True,
        'recipes': formatted_recipes
    }), 200

@app.route('/recipe/<id>', methods=['GET'])
@requires_auth(permission='get:recipe')
def get_recipe(id):
    """Get a recipe given its id"""
    recipe = Recipe.query.get(id)
    if not recipe:
        abort(404)

    response = jsonify({
        'success': True,
        'recipe': recipe.format()
    })
    return response

@app.route('/recipe', methods=['POST'])
@requires_auth(permission='post:recipe')
def post_recipe():
    '''Creates a new recipe'''
    json = request.get_json()

    data = json['recipe']
    if data.get('title') is None:
        abort(422,'Title is required')

    recipe = create_recipe_from_json(data)
    inserted_recipe = recipe.insert()

    response = jsonify({
        'success': True,
        'recipe': inserted_recipe.format()
    })

    return response, 201


@app.route('/recipe/<id>', methods=['DELETE'])
@requires_auth(permission='delete:recipe')
def delete_recipe(id):
    '''Delete a recipe by id'''
    recipe = Recipe.query.get(id)
    if recipe is None:
        abort(404)

    recipe.delete()
    response = jsonify( {
        'success': True
    })
    return response, 200


@app.route('/recipe/<id>', methods=['PATCH'])
@requires_auth(permission='patch:recipe')
def patch_recipe(id):
    original_recipe =  Recipe.query.get(id)
    if original_recipe is None:
        abort(404,'category does not exist')

    json_recipe = request.get_json()
    recipe = create_recipe_from_json(json_recipe['recipe'])

    if recipe.title is not None:
        original_recipe.name = recipe.title

    if recipe.description is not None:
        original_recipe.description = recipe.description

    if recipe.url is not None:
        original_recipe.slug = recipe.url

    original_recipe.update()

    response = jsonify({
        'success': True,
        'recipe': original_recipe.format()
    })
    return response, 200

# endregion


# region Category Controller
@app.route('/category', methods=['GET'])
@requires_auth(permission='get:category')
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


@app.route('/category/<id>', methods=['GET'])
@requires_auth(permission='get:category')
def get_category(id):
    """Get a category given its id"""
    category = Category.query.get(id)
    if not category:
        abort(404)

    response = jsonify({
        'success': True,
        'category': category.format()
    })
    return response


@app.route('/category', methods=['POST'])
@requires_auth(permission='post:category')
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


@app.route('/category/<id>', methods=['DELETE'])
@requires_auth(permission='delete:category')
def delete_category(id):
    '''Delete a category by id'''
    category = Category.query.get(id)
    if category is None:
        abort(404)

    category.delete()
    response = jsonify( {
        'success': True
    })
    return response, 200


@app.route('/category/<id>', methods=['PATCH'])
@requires_auth(permission='patch:category')
def patch_category(id):
    original_category =  Category.query.get(id)
    if original_category is None:
        abort(404,'category does not exist')

    json_category = request.get_json()
    category = create_category_from_json(json_category['category'])

    if category.description is not None:
        original_category.description = category.description

    if category.name is not None:
        original_category.name = category.name

    if category.slug is not None:
        original_category.slug = category.slug

    original_category.update()

    response = jsonify({
        'success': True,
        'category': original_category.format()
    })
    return response, 200
# endregion

# region Error Handlers
@app.errorhandler(422)
def unprocessable_entity(error):
    return jsonify(
        {
        'error': str(error),
        'success': False
        }
        ), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify(
        {
        'error': str(error),
        'success': False
        }
        ), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify(
        {
        'error': str(error),
        'success': False
        }
        ), 400


@app.errorhandler(AuthError)
def authentification_failed(AuthError):
    return jsonify({
        "success": False,
        "error": AuthError.status_code,
        "message": AuthError.error['description']
    }), AuthError.status_code
# endregion


# region Helper Methods
def create_category_from_json(json_data):
       return Category(name=json_data.get('name'),
                       description= json_data.get('description'),
                       slug=json_data.get('slug'))

def create_recipe_from_json(json_data):
    return Recipe(title=json_data.get('title'),
                    description=json_data.get('description'),
                    ingredients=json_data.get('ingredients'),
                    steps=json_data.get('steps'),
                    url=json_data.get('url'),
                    user_id=json_data.get('user_id'),
                    category_id = json_data.get('category_id')
                  )


def create_user_from_json(json_data):
    return User(username=json_data.get('username'))

# endregion

