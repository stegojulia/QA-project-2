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
c.execute('''DROP TABLE IF EXISTS sentences''')
c.execute('''CREATE TABLE IF NOT EXISTS sentences
             (id integer AUTO_INCREMENT PRIMARY KEY, en_sentence text, es_sentence text)''')


# Save (commit) the changes
conn.commit()



from app import app,Sentences,db


class TestBase(TestCase):
    def create_app(self):

        return app
    
    def setUp(self):
        sentence1 = Sentences(id=1057,en_sentence="You don't like love stories.", es_sentence="No le gustan las historias de amor.")
        sentence2 = Sentences(id=313,en_sentence='They say love is blind', es_sentence="Se dice que el amor es ciego.")
        sentence3 = Sentences(id=3094,en_sentence='Love and Peace.', es_sentence="Amor y paz.")
        db.session.add(sentence1)
        db.session.add(sentence2)
        db.session.add(sentence3)
        db.session.commit()

        stmt = select('*').select_from(Sentences)
        result = db.session.execute(stmt).fetchall()
        
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):
    def test_sentence(self):
        response = self.client.post(
            url_for('generate_sentence'), data="amor", follow_redirects=True
        )

        self.assertIn(response.data, [(bytes(i.es_sentence,'utf-8')) for i in db.session.query(Sentences).all()])
