from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_word(self):
        with patch("app.get_word") as g:
            with patch("app.get_sentence") as p1:
                with patch("app.get_learning") as p2:
                    g.return_value.text = "abuela"
                    p1.return_value.text = "La abuela bajó del autobús."
                    p2.return_value.text = "2021-02-22"

                    response = self.client.get(url_for("home"))
                    self.assertIn(b'<!DOCTYPE html>\n<html>\n    <body>\n        <p>version A</p>\n        <h1>Your word:</h1>\n        <h2>abuela</h2>\n\n        <h1>Your sentence:</h1>\n        <h2>La abuela baj\xc3\xb3 del autob\xc3\xbas.</h2>\n\n        <h1>Last viewed:</h1>\n        <h2>2021-02-22</h2>\n    </body>\n\n\n\n\n\n</html>', response.data) 
