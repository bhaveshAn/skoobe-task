from flask_restful import Resource, reqparse
from models.publisher import Publisher
from models.genre import Genre
from flask import jsonify, request 


class PublisherList(Resource):

    def get(self):
        return {'publisher': [x.json() for x in Publisher.query.all()]}

    def post(self):
        json_data = request.get_json(force=True)

        publisher = Publisher(
            json_data['name'],
            json_data['weight']
        )

        try:
            publisher.save()
        except Exception as e:
            return {'message': 'An error occurred inserting into db: {}'.format(e)}, 500

        return {'risk_type': publisher.json()}, 201

class PublisherDetail(Resource):

    def get(self, _id):
        try:
            publisher = Publisher.query.filter_by(id=_id).first()
            genres = []
            for genre in Genre.query.filter_by(publisher_id=_id):
                genre_obj = {}
                genre_obj['id'] = genre.id
                genre_obj['name'] = genre.name
                genre_obj['bid'] = genre.bid
                genre_obj['score'] = genre.score
                genres.append(genre_obj)
            response  = {"publisher": publisher.json(), 'genres': genres}
            return jsonify(response)
        except AttributeError:
            return "No such Publisher"


    def delete(self, _id):
        publisher = Publisher.query.filter_by(id=_id)

        status = 404
        message = 'Publisher not found'
        if publisher:
            publisher.delete()
            status = 200
            message = 'Publisher deleted'

        return {'message': message}, status
