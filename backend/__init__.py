from flask_restplus import Api
from flask import Blueprint

# import controllers
from .main.controllers.health_controller import api as health_ns
from .main.controllers.category_controller import api as category_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS RECIPES API',
          version='1.0',
          description='A flask Restplus API for managing recipes'
          )

# set resources main route
api.add_namespace(health_ns, path='/health')
api.add_namespace(category_ns, path='/category')
