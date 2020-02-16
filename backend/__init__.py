from flask_restplus import Api
from flask import Blueprint

from .main.controllers.health_controller import api as health_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS RECIPES API',
          version='1.0',
          description='A flask Restplus API for managing recipes'
          )

api.add_namespace(health_ns, path='/health')
