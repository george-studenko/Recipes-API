from flask_testing import TestCase
import warnings
from infraestructure.database import  db
from api.controllers import app
from infraestructure.config import bearer_tokens


class BaseTestCase(TestCase):
    """ Base Tests """
    cook_bearer_token = {
        'Authorization': bearer_tokens['cook']
    }
    def create_app(self):
        app.config.from_object('infraestructure.config.Test_Config')
        return app

    def setUp(self):
        warnings.filterwarnings("ignore")

        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
