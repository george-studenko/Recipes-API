from flask_sqlalchemy import SQLAlchemy

database_name = 'recipesDB'
database_host = 'localhost:5432'
database_path = 'postgres://{}/{}'.format(database_host, database_name)

db = SQLAlchemy

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

setup_db(app)


