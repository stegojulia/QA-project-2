use spanish_app;

create table sentences
select en_sentences.en_sentence, es_sentences.es_sentence
from en_sentences
join links
on en_sentences.id=links.id_1
join es_sentences 
on es_sentences.id=links.id_2;

ALTER TABLE sentences ADD id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;

SELECT * FROM vocab;

CREATE TABLE review (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, word VARCHAR(200),
revision_date DATE DEFAULT NOW());