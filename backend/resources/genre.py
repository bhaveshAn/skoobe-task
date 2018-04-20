from flask_restful import Resource, reqparse
from flask import jsonify, request
from models.genre import Genre
from models.book import Book
from models.publisher import Publisher


class GenreList(Resource):

    def get(self):
        return {'genres': [x.json() for x in Genre.query.all()]}

    def post(self):
        json_data = request.get_json(force=True)
        publisher = Publisher.query.filter_by(name=json_data['publisher_name']).first()
        publisher_id = publisher.id
        weight = publisher.weight
        score = int(json_data['bid']) * int(weight)
        

        genre = Genre(
            json_data['name'],
            publisher_id,
            int(json_data['bid']),
            score
        )

        try:
            genre.save()
        except Exception as e:
            return {'message': 'An error occurred inserting into db: {}'.format(e)}, 500

        return genre.json(), 200


class GenreDetail(Resource):

    def get(self, _id):
        try:
            genre = Genre.query.filter_by(id=_id).first()
            books = []
            for book in Book.query.filter_by(genre_id=_id):
                book_obj = {}
                book_obj['id'] = book.id
                book_obj['title'] = book.title
                book_obj['picture_url'] = book.picture_url
                book_obj['hyperlink'] = book.hyperlink
                book_obj['publisher_id'] = book.publisher_id
                books.append(book_obj)
            response  = {"genre": genre.json(), 'books': books}
            return jsonify(response)
        except AttributeError:
            return "No such Genre"

    def delete(self, _id):
        genre = Genre.query.filter_by(id=_id)

        status = 404
        message = 'Field not found.'
        if genre:
            status = 200
            message = 'Field deleted'
            genre.delete()

        return {'message': message}, status
