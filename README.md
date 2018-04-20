# Sponsored Book Search Auctions By Skoobe.de

> A Vue.js project

## Decoupled Structure

- Flask Backend

- Vue.js Frontend

## Installation
 
``` bash

cd skoobe-task
 
# install dependencies

# Create Virtual Environment
virtualenv venv

# Activate Virtual Environment
source venv/bin/activate

pip install -r backend/requirements.txt
npm install

# to run backend at localhost:5000
python backend/app.py

# to run frontend at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

## API Endpoints
``` bash

# GET and POST Publisher
http://localhost:5000/v1/publishers

# Example Body for POST
{
"name": String,
"weight": String
}


# GET and POST Genre
http://localhost:5000/v1/genres

# Example Body for POST
{
"name": String,
"bid": Integer,
"publisher_name": String
}

# GET and POST Book
http://localhost:5000/v1/books

# Example Body for POST
{
"title": String,
"picture_url": String,
"hyperlink": String,
"publisher_name": String,
"genre_name": String
}

# GET PublisherDetail
http://localhost:5000/v1/publishers/<int:id>

# GET GenreDetail
http://localhost:5000/v1/genre/<int:id>

# GET BookDetail
http://localhost:5000/v1/book/<int:id>

## GET SearchList
http://localhost:5000/v1/book/<search_query>

## Vue Frontend

For Romance Genre

[http://localhost:8080/#/romance](http://localhost:8080/#/romance) 
& 
[http://localhost:8080/#/show romance books](http://localhost:8080/#/show romance books)

Gives same results

For Science Fiction

[http://localhost:8080/#/science fiction](http://localhost:8080/#/science fiction)

```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).












