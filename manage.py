from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from backend.main import create_app, db
from backend import blueprint
import unittest
from backend.main.models import recipe, category, comment, language

app = create_app()
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs unit test."""
    tests = unittest.TestLoader().discover('backend/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    print('Tests were run using the db:',app.config['SQLALCHEMY_DATABASE_URI'])
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
