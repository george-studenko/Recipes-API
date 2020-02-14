from main import db

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