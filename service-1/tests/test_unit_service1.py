import unittest
from unittest.mock import patch
from flask_testing import TestCase
from flask import url_for
import datetime
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from flask import Flask
import os

import sqlite3
conn = sqlite3.connect('test.db')

c = conn.cursor()

# Create table review
c.execute('''DROP TABLE IF EXISTS review''')
c.execute('''CREATE TABLE IF NOT EXISTS review
             (id integer AUTO_INCREMENT PRIMARY KEY, word text, revision_date text)''')

# Save (commit) the changes
conn.commit()

from app import app,db


class TestBase(TestCase):
    def create_app(self):

        return app
    
    def setUp(self):
        db.create_all()
        
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):
    def test_words(self):
        with patch("app.get_word") as g:
            with patch("app.get_sentence") as p1:
                with patch("app.get_learning") as p2:
                    g.return_value.text = "amor"
                    p1.return_value.text = "love"
                    p2.return_value.text = "New word"
                    version = 'version B'
                    response = self.client.get(url_for("home"))
                    self.assertIn(b'<!DOCTYPE html>\n<html>\n    <body>\n        <p>version A</p>\n        <h1>Your word:</h1>\n        <h2>amor</h2>\n\n        <h1>Your sentence:</h1>\n        <h2>love</h2>\n\n        <h1>Last viewed:</h1>\n        <h2>New word</h2>\n    </body>\n\n\n\n\n\n</html>', response.data)

