from flask_restful import Resource, reqparse
from flask import jsonify, request
from models.genre import Genre
from models.book import Book
from models.publisher import Publisher
from textblob import TextBlob


class SearchList(Resource):

    def get(self, search_query):
        words = TextBlob(search_query)
        if 'romance' in words:
            genre_name = 'Romance'
        elif 'science' in words and 'fiction' in words:
            genre_name = 'Science Fiction'
        elif 'science' in words:
            genre_name = 'Science'
        elif 'satire' in words:
            genre_name = 'Satire'
        elif 'drama' in words:
            genre_name = 'Drama'
        elif 'action' in words or 'adventure' in words:
            genre_name = 'Action'
        elif 'mystery' in words:
            genre_name = 'Mystery'
        elif 'horror' in words:
            genre_name = 'Horror'
        elif 'help' in words:
            genre_name = 'Self Help'
        elif 'health' in words:
            genre_name = 'Health'
        elif 'guide' in words:
            genre_name = 'Guide'
        elif 'travel' in words:
            genre_name = 'Travel'
        elif 'kid' in words or 'kids' in words or 'children' in words:
            genre_name = 'Kids'
        elif 'religion' in words or 'religious' in words or 'spiritual' in words or 'spirituality' in words:
            genre_name = 'Religion'
        elif 'history' in words or 'ancient' in words or 'historical' in words:
            genre_name = 'History'
        elif 'math' in words or 'mathematics' in words or 'mathematical' in words:
            genre_name = 'Math'
        elif 'drama' in words:
            genre_name = 'Drama'
        elif 'comic' in words or 'comics' in words:
            genre_name = 'Comic'
        elif 'dictionary' in words or 'dictionaries' in words:
            genre_name = 'Dictionary'
        else:
            genre_name = words[0].title()

        top_publishers = []
        for sponsored in Genre.query.filter_by(name=genre_name).order_by(Genre.score.desc()):
            publisher = Publisher.query.filter_by(id=sponsored.publisher_id).first()
            for book in Book.query.filter_by(publisher_id=sponsored.publisher_id).all():
                book_obj = {}
                book_obj['title'] = book.title
                book_obj['picture_url'] = book.picture_url
                book_obj['hyperlink'] = book.hyperlink
                book_obj['genre_name'] = genre_name
                book_obj['publisher_name'] = publisher.name
                top_publishers.append(book_obj)
        # rest = Genre.query.filter_by(name=genre_name).first()
        low_publishers = []
        for sponsored in Genre.query.filter_by(name=genre_name).all():
            publisher = Publisher.query.filter_by(id=sponsored.publisher_id).first()
            for book in Book.query.filter_by(genre_id=sponsored.id).all():
                book_obj = {}
                book_obj['title'] = book.title
                book_obj['picture_url'] = book.picture_url
                book_obj['hyperlink'] = book.hyperlink
                book_obj['genre_name'] = genre_name
                book_obj['publisher_name'] = publisher.name
                low_publishers.append(book_obj)
        
        return {'top_publishers': top_publishers, 'low_publishers': low_publishers}

