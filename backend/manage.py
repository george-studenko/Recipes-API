from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from main import create_app, db
from models import recipe, category, comment, language

app = create_app()
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    #APP.run(host='0.0.0.0', port=8080, debug=True)
    manager.run()
