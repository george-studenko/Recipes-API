from backend.main import db

class Category(db.Model):
    __tablename__ = 'Category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    slug = db.Column(db.String)

    recipes = db.relationship('Recipe', backref='Category')

    def __init__(self, name, description= None, slug= None):
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
            'category':{
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'slug': self.slug
            }
        }
