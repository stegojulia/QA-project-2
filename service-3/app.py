from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import random
import pymysql
import mysql.connector
import datetime
import requests
from sqlalchemy.ext.automap import automap_base


app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://julia:julia123@34.105.5.17:3306/spanish_app"

db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Vocab = Base.classes.vocab


@app.route('/sentence/', methods=['GET', 'POST'])
def generate_sentence():
    word = request.data.decode('utf-8')
    translation = db.session.query(Vocab).filter(Vocab.en_word==word)
    words = [i for i in translation][0]
    return  Response(str(words.es_word), mimetype="text/plain")


if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0', port=5002)