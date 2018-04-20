from flask_restful import Resource, reqparse
from flask import jsonify, request
from models.genre import Genre
from models.book import Book
from models.publisher import Publisher


class BookList(Resource):

    def get(self):
        return {'books': [x.json() for x in Book.query.all()]}

    def post(self):
        json_data = request.get_json(force=True)
        publisher = Publisher.query.filter_by(name=json_data['publisher_name']).first()
        publisher_id = publisher.id
        genre = Genre.query.filter_by(name=json_data['genre_name']).first()
        genre_id = genre.id
        

        book = Book(
            json_data['title'],
            json_data['picture_url'],
            json_data['hyperlink'],
            genre_id,
            publisher_id
        )

        try:
            book.save()
        except Exception as e:
            return {'message': 'An error occurred inserting into db: {}'.format(e)}, 500

        return book.json(), 200


class BookDetail(Resource):

    def get(self, _id):
        try:
            book = Book.query.filter_by(id=_id).first()
            return book.json()
        except AttributeError:
            return "No such Genre"

    def delete(self, _id):
        book = Book.query.filter_by(id=_id)

        status = 404
        message = 'Field not found.'
        if genre:
            status = 200
            message = 'Field deleted'
            genre.delete()

        return {'message': message}, status

    def put(self, _id):
        json_data = request.get_json(force=True)

        book = Book.query.filter_by(id=_id).first()
        publisher = Publisher.query.filter_by(name=json_data['publisher_name']).first()
        publisher_id = publisher.id
        genre = Genre.query.filter_by(name=json_data['genre_name']).first()
        genre_id = genre.id
        

        book = Book(
            json_data['title'],
            json_data['picture_url'],
            json_data['hyperlink'],
            genre_id,
            publisher_id
        )
        status = 200
        if book:
            book.title = json_data['title']
            book.picture_url = json_data['picture_url']
            book.hyperlink = json_data['hyperlink']
            book.genre_id = genre_id
            book.publisher_id = publisher_id
            book.commit()
        else:
            book = Book(
                json_data['title'],
                json_data['picture_url'],
                json_data['hyperlink'],
                genre_id,
                publisher_id
            )
            status = 201
            book.save()

        return book.json(), status
