import os
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import random
import pymysql
import mysql.connector
import datetime
import requests
from sqlalchemy.ext.automap import automap_base


app = Flask(__name__)

app.config['SECRET_KEY'] = getenv("KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Sentences = Base.classes.sentences


@app.route('/sentence/', methods=['GET', 'POST'])
def generate_sentence():
    word = request.data.decode('latin-1')
    like_word = '%' + word + '%'
    all_sentences = db.session.query(Sentences).filter(Sentences.es_sentence.like(like_word))
    sentences = [i.es_sentence for i in all_sentences]
    try:
       return Response(str(random.choice(sentences)))
    except:
       return "Make up your own sentence"


if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0', port=5002)
