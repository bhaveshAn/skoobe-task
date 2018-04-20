from db import db
from models.publisher import Publisher
from models.genre import Genre


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    picture_url = db.Column(db.String(150))
    hyperlink = db.Column(db.String(150))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))


    def __init__(self, title, picture_url, hyperlink, genre_id, publisher_id):
        self.title = title
        self.picture_url = picture_url
        self.hyperlink = hyperlink
        self.genre_id = genre_id
        self.publisher_id = publisher_id
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def commit(self):
        db.session.commit()

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'picture_url': self.picture_url,
            'hyperlink': self.hyperlink,
            'genre_id': self.genre_id,
            'publisher_id': self.publisher_id
        }

    def delete(self):
        db.session.delete(self)
        db.session.commit()
