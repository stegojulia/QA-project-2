from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_word(self):
        with patch(word_get()) as g:
            with patch(sentence_post(word)) as p1:
                with patch(learning_post) as p2:
                    g.return_value.text = "abuela"
                    p1.return_value = "La abuela bajó del autobús."
                    p2.return_value = "2021-02-22"

                    response = self.client.get(url_for("home"))
                    self.assertIn('<h1>Your word:</h1><h2>método</h2><h1>Your sentence:</h1><h2>¿Qué método has usado para dejar de fumar?</h2>]<h1>Last viewed:</h1>   <h2>2021-02-22</h2><h2>2021-02-22</h2></body>', response.data) 
