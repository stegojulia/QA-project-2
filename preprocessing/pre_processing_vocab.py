import csv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

words = []

with open("vocab.csv", encoding='latin-1') as vocab:
    data = csv.reader(vocab, delimiter=",", quotechar='"')
    for row in data:
        words.append(row)

for i in range(0,10):
    print(words[i])

#sqlalchemy
engine = create_engine('mysql+pymysql://julia:julia123@localhost/spanish_app', echo=True)

Base = declarative_base()

class Vocab(Base):
    __tablename__ = 'vocab'
    id = Column(Integer, primary_key=True)
    es_word = Column(String(250))
    en_word = Column(String(250))

    def __repr__(self):
        return "<es_sentences(es_word='%s', en_word='%s')>" % (
                                self.es_word, self.en_word)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

for row in words:
    entry = Vocab(es_word = row[0], en_word=row[1])
    session.add(entry)
    session.commit()