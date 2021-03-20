import csv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import pymysql

import time
start_time = time.time()

#preprocess sentences and links data

sentences_list=[]
spa_sentences_list = []
links_list = []

with open("preprocessing/eng_sentences.tsv") as file:
    data = csv.reader(file, delimiter="\t", quotechar='"')
    for row in data:
        sentences_list.append(row)

for row in sentences_list:
row.remove(row[1])

with open("preprocessing/spa_sentences.tsv") as spa_file:
    data = csv.reader(spa_file, delimiter="\t", quotechar='"')
    for row in data:
        spa_sentences_list.append(row)

for row in spa_sentences_list:
    row.remove(row[1])

with open("preprocessing/links.csv") as links:
    data = csv.reader(links, delimiter="\t", quotechar='"')
    for row in data:
        links_list.append(row)

#transfer data to mysql tables
connection = pymysql.connect(host='localhost', user='julia', password='julia123', db='spanish_test')

cursor = connection.cursor()

for row in sentences_list:
    try:
        sql = "INSERT INTO `en_sentences` (`id`, `en_sentence`) VALUES (%s, %s)"
        id = row[0]
        en_sentence=row[1]
        cursor.execute(sql, (id,en_sentence))
    except:
        continue

for row in spa_sentences_list:
    try:
        sql = "INSERT INTO `es_sentences` (`id`, `es_sentence`) VALUES (%s, %s)"
        id = row[0]
        en_sentence=row[1]
        cursor.execute(sql, (id,es_sentence))
    except:
        continue

for row in links_list:
    if int(row[0]) > 47193 and int(row[0]) < 413869:
        sql = "INSERT INTO `links` (`id_1`, `id_2`) VALUES (%s, %s)"
        id_1 = int(row[0])
        id_2 = int(row[1])
        print (id_1, id_2)
        cursor.execute(sql, (id_1, id_2))

connection.commit()
