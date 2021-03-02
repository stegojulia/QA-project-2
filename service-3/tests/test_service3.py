import unittest
from flask_testing import TestCase
from flask import url_for
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from flask import Flask
import os

import sqlite3
conn = sqlite3.connect('test.db')

c = conn.cursor()

# Create table
c.execute('''DROP TABLE IF EXISTS vocab''')
c.execute('''CREATE TABLE IF NOT EXISTS vocab
             (id integer AUTO_INCREMENT PRIMARY KEY, es_word text, en_word text)''')



# Save (commit) the changes
conn.commit()



from app import app,Vocab,db


class TestBase(TestCase):
    def create_app(self):

        return app
    
    def setUp(self):
        word1 = Vocab(id=1,es_word='abuela', en_word="grandmother")
        word2 = Vocab(id=2,es_word='abuelo', en_word="grandfather")
        word3 = Vocab(id=3,es_word='madre', en_word="mother")
        db.session.add(word1)
        db.session.add(word2)
        db.session.add(word3)
        db.session.commit()

        stmt = select('*').select_from(Vocab)
        result = db.session.execute(stmt).fetchall()
        
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):
    def test_abuelo(self):
        response = self.client.post(
            url_for('generate_sentence'), data="grandfather", follow_redirects=True
        )

        self.assertEqual(response.data, b'abuelo')

class TestResponse(TestBase):
    def test_abuela(self):
        response = self.client.post(
            url_for('generate_sentence'), data="grandmother", follow_redirects=True
        )

        self.assertEqual(response.data, b'abuela')

class TestResponse(TestBase):
    def test_madre(self):
        response = self.client.post(
            url_for('generate_sentence'), data="mother", follow_redirects=True
        )

        self.assertEqual(response.data, b"madre")
