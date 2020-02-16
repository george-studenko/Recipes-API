from backend.main import db

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    recipes = db.relationship('Recipe', backref='user')


    def __init__(self, id, username):
        #self.id = id
        self.username = username