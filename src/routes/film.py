from flask import Blueprint
from flask_restful import Api

from resources import FilmResource, TopResource

routes = [
    '/film/<string:id>',
    '/film/',
]

FILM_BLUEPRINT = Blueprint("film", __name__)
Api(FILM_BLUEPRINT).add_resource(
    FilmResource, *routes
)
TOP_BLUEPRINT = Blueprint("top", __name__)
Api(TOP_BLUEPRINT).add_resource(
    TopResource, '/top/'
)
