from flask_sqlalchemy import SQLAlchemy

import json

database_name = 'recipesDB'
database_host = 'localhost:5432'
database_path = 'postgres://{}/{}'.format(database_host, database_name)

db = SQLAlchemy

def setup_db(app, database_path = database_path):
    pass

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

    def __init__(self, title, description, ingredients, steps, url, language, user, category):
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


class Category(db.Model):
    __tablename__ = 'Category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    slug = db.column(db.String)
    language = db.relationship('language', backref='Language')

    def __init__(self, name, description, slug, language):
        self.language = language
        self.slug = slug
        self.name = name
        self.description = description


#     recipe_id = db.Column(db.Integer, db.ForeignKey('Recipe.id'))

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
            'name': self.name,
            'description': self.description,
            'slug': self.slug,
            'language': self.language
        }

class Comment(db.Model):
    __tablename__ = 'Comment'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipe.id'))

    def __init__(self, comment, recipe_id):
        self.comment = comment
        self.recipe_id = recipe_id

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
            'comment': self.comment,
            'recipe_id': self.recipe_id
        }

