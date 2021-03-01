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
Review = Base.classes.review

@app.route('/learning/', methods=['GET', 'POST'])
def learning():
    word = request.data.decode('latin-1')
    like_word = '%' + word + '%'
    try:
        all_records = db.session.query(Review).filter(Review.word==word)
        records = [i.revision_date for i in all_records]
        record = str(records[-2])
    except:
        return "New word"
    return Response(str(record))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)