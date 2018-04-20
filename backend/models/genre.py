from db import db
from models.publisher import Publisher


class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    bid = db.Column(db.Integer)
    score = db.Column(db.Integer)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))


    def __init__(self, name, publisher_id, bid=0, score=0):
        self.name = name
        self.bid = bid
        self.score = score
        self.publisher_id = publisher_id
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def commit(self):
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'bid': self.bid,
            'score': self.score,
            'publisher_id': self.publisher_id
        }

    def delete(self):
        db.session.delete(self)
        db.session.commit()
