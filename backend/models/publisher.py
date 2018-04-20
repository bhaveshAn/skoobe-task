from db import db


class Publisher(db.Model):
    __tablename__ = 'publisher'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    weight = db.Column(db.Integer)

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        
    def save(self):
        db.session.add(self)
        db.session.commit()

    def commit(self):
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'weight': self.weight
        }

    def delete(self):
        db.session.delete(self)
        db.session.commit()
