import os
from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
import models

from resources.publisher import PublisherList, PublisherDetail
from resources.genre import GenreList, GenreDetail
from resources.book import BookList, BookDetail
from resources.search import SearchList


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', default='sqlite:///memory.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'mysecret'
api = Api(app)

@app.route('/')
def index():
    return "Server Running"

# GET, DELETE
api.add_resource(PublisherDetail, '/v1/publisher/<int:_id>')
# GET, POST
api.add_resource(PublisherList, '/v1/publishers')

# GET, DELETE
api.add_resource(GenreDetail, '/v1/genre/<int:_id>')
# GET, POST
api.add_resource(GenreList, '/v1/genres')

# GET, DELETE
api.add_resource(BookDetail, '/v1/book/<int:_id>')
# GET, POST
api.add_resource(BookList, '/v1/books')

# GET
api.add_resource(SearchList, '/v1/search/<search_query>')


if __name__ == '__main__':
    from db import db
    db.init_app(app)

    # Create db tables if they don't exist
    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run(debug=True)
