[![Build Status](https://travis-ci.com/aitorbouzas/imdb-flask.svg?branch=master)](https://travis-ci.com/aitorbouzas/imdb-flask)

# IMDB top Flask + React + web scraping

This repository contains several components that will allow you to create a small app containing the 250 top films from IMDB.
The backend is made with Flask, the simple frontend is made with React and the scraping of the top films is made with requests and BeautifulSoup libraries from Python.

## Pre-requisites

 - Docker
 - Docker-compose

## Basic start

    make server.install    # It installs all python requirements for backend
    make database.init     # Prepares database
    make database.migrate  # Creates migration scripts
    make database.upgrade  # Uses migration scripts
    make web.build         # Builds frontend image
    make web.d             # Starts the entire stack as a daemon
    python scrap/scrap.py  # Runs the scraper and updates the DB

Backend should be available at [localhost:5000](http://localhost:5000) and frontend at [localhost:3000](http://localhost:3000).

## Flask backend
--------------------

The Flask backend is launched through a docker-compose that contains two images: a python-3.6 and a postgresql.
For testing purposes another database image has been configured in the docker compose. To run tests just run:

    make server.test
    make server.flake8

In addition Travis-CI has been configured in this repo so that the CI is automatically launched every PR.

The backend has been made with: 

 - Flask
 - SQLAlchemy
 - Swagger
 - Flasgger
 - PostgreSQL

### API endopints

 - `/api/spec`: swagger specifications
 - `/api/apidocs`: flasgger UI for testing API
 - `/api/top/`: 
   - GET - gets the top 250 films from IMDB
 - `/api/film/`:
   - POST - creates new film
 - `/api/film/<string:id>`:
   - GET - gets film info
   - UPDATE - updates film info
   - DELETE - deletes film

## React.js frontend
--------------------

Made with create-react-app basic sample. It'll show the top films and allow you to delete them.

# Roadmap

- Security for backend
- Allow updating a film in frontend