from infraestructure.database import db


class Recipe(db.Model):
    __tablename__ = 'Recipe'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    ingredients = db.Column(db.ARRAY(db.String(150)))
    steps = db.Column(db.ARRAY(db.String(1000)))
    url = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey('Category.id'),
        nullable=False)

    def __init__(self, title, description, ingredients,
                 steps, url, user_id, category_id):
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.steps = steps
        self.url = url
        self.user_id = user_id
        self.category_id = category_id

    def insert(self):
        db.session.add(self)
        db.session.flush()
        db.session.commit()
        return self

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
            'user_id': self.user_id,
            'category_id': self.category_id
        }


class Category(db.Model):
    __tablename__ = 'Category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    slug = db.Column(db.String)

    recipes = db.relationship('Recipe', backref='Category')

    def __init__(self, name, description=None, slug=None):
        self.slug = slug
        self.name = name
        self.description = description

    def insert(self):
        db.session.add(self)
        db.session.flush()
        db.session.commit()
        return self

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'slug': self.slug
        }


class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    recipes = db.relationship('Recipe', backref='user')

    def insert(self):
        db.session.add(self)
        db.session.flush()
        db.session.commit()
        return self

    def format(self):
        return {
            'id': self.id,
            'username': self.username
        }

    def __init__(self, username):
        self.username = username
