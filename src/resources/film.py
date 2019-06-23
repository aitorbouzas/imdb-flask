from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import FilmRepository
from util import parse_params


class TopResource(Resource):
    """ Top list resource """

    @staticmethod
    @swag_from("../sw/top/GET.yml")
    def get():
        films = FilmRepository.get_all()
        films_json = [film.json for film in films]
        return jsonify({"films": films_json})


class FilmResource(Resource):
    """ Film resources """

    @staticmethod
    @swag_from("../sw/film/GET.yml")
    def get(id):
        film = FilmRepository.get(id=id)
        return jsonify({"film": film.json})

    @staticmethod
    @parse_params(
        Argument(
            "name",
            location="json",
            required=True,
            help="Name of the film"
        ),
        Argument(
            "year",
            location="json",
            required=True,
            help="Year of publication"
        ),
        Argument(
            "pos",
            location="json",
            required=True,
            help="Position in IMDB's top"
        ),
        Argument(
            "rating",
            location="json",
            required=True,
            help="Rating in IMDB"
        ),
        Argument(
            "url",
            location="json",
            required=True,
            help="URL of IMDB's film"
        ),
        Argument(
            "image",
            location="json",
            required=True,
            help="URL of film's image in IMDB"
        ),
    )
    @swag_from("../sw/film/POST.yml")
    def post(name, year, pos, rating, url, image):
        film = FilmRepository.create(
            name=name,
            year=year,
            pos=pos,
            rating=rating,
            url=url,
            image=image,
        )
        return jsonify({"film": film.json})

    @staticmethod
    @parse_params(
        Argument(
            "vals",
            location="json",
            required=True,
            help="Dict containing vals to update"
        ),
    )
    @swag_from("../sw/film/PUT.yml")
    def put(id, vals):
        fr = FilmRepository()
        film = fr.update(id, vals)
        return jsonify({"film": film.json})

    @staticmethod
    @swag_from("../sw/film/DELETE.yml")
    def delete(id):
        fr = FilmRepository()
        fr.delete(id)
        return jsonify({"message": "Deleted succesfully"})
