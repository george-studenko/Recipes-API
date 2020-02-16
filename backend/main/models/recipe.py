from backend.main import db


class Recipe(db.Model):
    __tablename__ = 'Recipe'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    ingredients = db.Column(db.ARRAY(db.String(150)))
    steps = db.Column(db.ARRAY(db.String(1000)))
    url = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'), nullable=False)

    def __init__(self, title, description, ingredients,
                 steps, url, language, user_id, category):
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.steps = steps
        self.url = url
        self.language = language
        self.user_id = user_id
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
            'user_id': self.user_id,
            'category': self.category
        }