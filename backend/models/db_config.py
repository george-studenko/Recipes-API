from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


database_name = 'recipesDB'
database_host = 'localhost:5432'
database_path = 'postgres://{}/{}'.format(database_host, database_name)

db = SQLAlchemy


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    print('db.app: ',app)
    db.init_app(SQLAlchemy,app)
    print('db.init EXECUTED')
    #migrate = Migrate(app, db)




