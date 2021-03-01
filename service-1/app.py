from flask import Flask, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
import random
import pymysql
import mysql.connector
import datetime
import requests
from sqlalchemy.ext.automap import automap_base
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:julia123@database:3306/spanish_app"

db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Review = Base.classes.review

def get_word():
    word = requests.get("http://service-2:5012/word")
    return word 

def get_sentence(word):
    return requests.post("http://service-3:5002/sentence/", data = word.text)

def get_learning(word):
    return requests.post("http://service-4:5003/learning/", data = word.text)

@app.route('/', methods=['GET', 'POST'])
def home():
    word = get_word()
    sentence = get_sentence(word)
    learning = get_learning(word)
    review_data = Review(word=word.text, revision_date=datetime.datetime.now())
    db.session.add(review_data)
    db.session.commit()
    version = 'version B'
    return render_template('home.html', word=word.text, sentence=sentence.text, learning=learning.text, version=version)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5011)
