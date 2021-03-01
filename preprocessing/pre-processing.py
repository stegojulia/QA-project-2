import csv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

sentences_list=[]

with open("preprocessing/eng_sentences.tsv") as file:
    data = csv.reader(file, delimiter="\t", quotechar='"')
    for row in data:
        sentences_list.append(row)

for row in sentences_list:
    row.remove(row[1])

spa_sentences_list = []
links_list = []

with open("preprocessing/spa_sentences.tsv") as spa_file:
    data = csv.reader(spa_file, delimiter="\t", quotechar='"')
    for row in data:
        spa_sentences_list.append(row)

for row in spa_sentences_list:
    row.remove(row[1])

for i in range(0,10):
    print(spa_sentences_list[i])


with open("preprocessing/links.csv") as links:
    data = csv.reader(links, delimiter="\t", quotechar='"')
    for row in data:
        links_list.append(row)


#sqlalchemy
engine = create_engine('mysql+pymysql://julia:julia123@localhost/spanish_app', echo=True)

Base = declarative_base()

class En_sentences(Base):
    __tablename__ = 'en_sentences'

    id = Column(Integer, primary_key=True)
    en_sentence = Column(String(500))

    def __repr__(self):
        return "<en_sentences(id='%s', en_sentence='%s')>" % (
                                self.id, self.en_sentence)

class Es_sentences(Base):
    __tablename__ = 'es_sentences'

    id = Column(Integer, primary_key=True)
    es_sentence = Column(String(600))

    def __repr__(self):
        return "<es_sentences(id='%s', es_sentence='%s')>" % (
                                self.id, self.es_sentence)


class Links(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    id_1 = Column(Integer)
    id_2 = Column(Integer)

    def __repr__(self):
        return "<es_sentences(id_1='%s', id_2='%s')>" % (
                                self.id_1, self.id_2)

Base.metadata.create_all(engine)




Session = sessionmaker(bind=engine)
session = Session()


#for row in sentences_list:
#    if int(row[0]) > 1276:
#        entry = En_sentences(id = row[0], en_sentence=row[1])
#        session.add(entry)
#        session.commit()


for row in spa_sentences_list:
    entry = Es_sentences(id = row[0], es_sentence=row[1])
    session.add(entry)
    session.commit()

#for row in links_list:
#    if int(row[0]) > 47193 and int(row[0]) < 413869:
#        entry = Links(id_1 = row[0], id_2=row[1])
#        session.add(entry)
#        session.commit()