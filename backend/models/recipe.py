from backend.models.db_config import db


class Recipe(db.Model):
    __tablename__ = 'Recipe'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    ingredients = db.Column(db.ARRAY(db.String(150)))
    steps = db.Column(db.ARRAY(db.String(1000)))
    url = db.Column(db.String)

    language = db.relationship('Language', backref='Language')
    user = db.relationship('User', backref='User')
    category = db.relationship('Category', backref='Category')

    def __init__(self, title, description, ingredients,
                 steps, url, language, user, category):
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.steps = steps
        self.url = url
        self.language = language
        self.user = user
        self.category = category

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'ingredients': self.ingredients,
            'steps': self.steps,
            'url': self.url,
            'language': self.language,
            'user': self.user,
            'category': self.category
        }