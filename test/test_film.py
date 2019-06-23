import json
import unittest

from models import Film
from models.abc import db
from repositories import FilmRepository
from server import server


class TestFilm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()
        cls.film_dict = {
            'name': 'Cadena perpetua',
            'year': 1994,
            'pos': 1,
            'rating': 9.2,
            'url': '.',
            'image': '.',
        }

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        FilmRepository.create(**self.film_dict)
        response = self.client.get("/api/film/1")

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        check_dict = self.film_dict.copy()
        check_dict['id'] = 1
        self.assertEqual(
            response_json,
            {"film": check_dict},
        )

    def test_create(self):
        response = self.client.post(
            "/api/film/",
            content_type="application/json",
            data=json.dumps(self.film_dict),
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        check_dict = self.film_dict.copy()
        check_dict['id'] = 1

        self.assertEqual(
            response_json,
            {"film": check_dict},
        )
        self.assertEqual(Film.query.count(), 1)

    def test_update(self):
        FilmRepository.create(**self.film_dict)

        film_update = {
            "vals": {
                'year': 1995,
            }
        }
        response = self.client.put(
            "/api/film/1",
            content_type="application/json",
            data=json.dumps(film_update),
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        check_dict = self.film_dict.copy()
        check_dict['id'] = 1
        check_dict['year'] = 1995

        self.assertEqual(
            response_json,
            {"film": check_dict},
        )
        film = FilmRepository.get(id=1)
        self.assertEqual(film.year, 1995)
