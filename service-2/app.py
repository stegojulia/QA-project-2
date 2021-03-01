import os
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import random
import pymysql
import mysql.connector
import datetime
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL",default="mysql+pymysql://julia:julia123@34.105.5.17:3306/spanish_app")

db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Vocab = Base.classes.vocab


@app.route('/word/', methods=['GET', 'POST'])
def generate_word():
    all_words = db.session.query(Vocab).all()
    random_result = random.choice(all_words)
    random_word = random_result.es_word
    return Response(random_word, mimetype="text/plain")

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5012)