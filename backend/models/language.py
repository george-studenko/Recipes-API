from backend.models.db_config import db

class Language(db.Model):
    __tablename__ = 'Language'

    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String)

    def __init__(self, language):
        self.language = language

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
            'language': self.language
        }
