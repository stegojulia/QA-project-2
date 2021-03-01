import os
import unittest
from flask_testing import TestCase
from flask import url_for
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from flask import Flask
from datetime import datetime, date


import sqlite3
conn = sqlite3.connect('test.db')

c = conn.cursor()

# Create table
c.execute('''DROP TABLE IF EXISTS review''')
c.execute('''CREATE TABLE IF NOT EXISTS review
             (id integer AUTO_INCREMENT PRIMARY KEY, word text, revision_date text)''')


# Save (commit) the changes
conn.commit()

from app import app,Review,db


class TestBase(TestCase):
    def create_app(self):
        return app
    
    def setUp(self):
        review1 = Review(id=1,word="amor", revision_date="2021, 2, 28")
        review2 = Review(id=2,word="perro", revision_date="2021, 2, 28")
        review3 = Review(id=3,word="perro", revision_date="2021, 2, 28")
        review4 = Review(id=4,word="padre", revision_date="2021, 2, 28")
        review5 = Review(id=5,word="padre", revision_date="2021, 2, 28")
        review6 = Review(id=6,word="padre", revision_date="2021, 2, 28")
        db.session.add(review1)
        db.session.add(review2)
        db.session.add(review3)
        db.session.add(review4)
        db.session.add(review5)
        db.session.add(review6)
        db.session.commit()

        stmt = select('*').select_from(Review)
        result = db.session.execute(stmt).fetchall()
        
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):
    def test_review_one(self):
        response = self.client.post(
            url_for('learning'), data="amor", follow_redirects=True
        )
        self.assertEqual(response.data, b"Review in 7 days")

class TestResponse(TestBase):
    def test_review_two(self):
        response = self.client.post(
            url_for('learning'), data="perro", follow_redirects=True
        )
        self.assertEqual(response.data, b"Review in 14 days")

class TestResponse(TestBase):
    def test_review_new(self):
        response = self.client.post(
            url_for('learning'), data="padre", follow_redirects=True
        )
        self.assertEqual(response.data, b"New word: review in 2 days")

class TestResponse(TestBase):
    def test_review_new(self):
        response = self.client.post(
            url_for('learning'), data="madre", follow_redirects=True
        )
        self.assertEqual(response.data, b"New word: review in 2 days")