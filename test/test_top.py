import json
import unittest

from models.abc import db
from repositories import FilmRepository
from server import server


class TestFilm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()
        cls.film_dict_1 = {
            'name': 'Cadena perpetua',
            'year': 1994,
            'pos': 1,
            'rating': 9.2,
            'url': '.',
            'image': '.',
        }
        cls.film_dict_2 = {
            'name': 'Cadena perpetua 2',
            'year': 1994,
            'pos': 1,
            'rating': 9.2,
            'url': '.',
            'image': '.',
        }
        cls.film_dict_3 = {
            'name': 'Cadena perpetua 3',
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
        FilmRepository.create(**self.film_dict_1)
        FilmRepository.create(**self.film_dict_2)
        FilmRepository.create(**self.film_dict_3)

        response = self.client.get("/api/top/")

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            len(response_json.get("films")),
            3,
        )
