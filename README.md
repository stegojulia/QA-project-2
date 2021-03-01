# Learn Spanish app
The function of this app is to facilitate learning of Spanish vocabulary. It generates Spanish words that are displayed to the user. The app also keeps tracks of when words were displayed and indicates if a new word is introduced to the user. 

# Design

## Brief
This app was created as part of DevOps Core Practical Project during a QA DevOps bootcamp in February 2021. The project aimed to create and deploy four interconnected services using the following technologies:

* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX

Services #2, #3, #4 were required to have two different implementations each to demonstrate swapping these implementations out without disruption.

## Services design

### Service #1

### Service #2
Service #2 generates

## Database design


<img src="Images/Houseplant Tracker - QA Project_1.png" alt="ERD" style="width:20;">


# Project management

## Workflow
A Trello board was the main project management tool used. The board developed along with the project as my knowledge increased. Initially, it only included user stories with main features. Later I was able to decompose each story into smaller tasks. In addition to the MVP elements, I also added additional tasks which can be carried out to expand the app. I updated the board daily. Several times it became clear that what I initially thought was essential was not as important - and vice versa, so I adjusted the plan accordingly.

<figure>
<img src="Images/trello-early.png" alt="Trello-board" style="width:20;">
<figcaption> Early version of the board with user stories. </figcaption>
</figure>

<figure>
<img src="Images/trello.png" alt="Trello-board" style="width:20;">
<figcaption> Trello board expanded with individual tasks </figcaption>
</figure>

## CI Pipeline

<img src="Images/CI-pipeline.png" alt="CI pipeline" class="center" style="width:20;">

## Risk assessment


<img src="Images/risk-assessment-matrix.png" alt="risk assessment matrix" class="center" style="width:20;">

<img src="Images/risk-assessment-list.png" alt="risk assessment list" class="center" style="width:20;">

# Development

## Data pre-processing
The app required a database of Spanish words and sentences with English translation. Vocabulary list and translations were obtained from NCELP (2019). *Full list: words within the 2000 most frequent in Spanish without entries in AQA GCSE Spanish vocabulary specification (by word class)*. National Centre for Excellence for Language Pedagogy: University of York, UK. The list is available under CC BY-NC-SA 4.0. The sentences with translations come from Tatoeba, https://tatoeba.org, released under CC-BY 2.0 FR. Tatoeba contains sentences in 392 languages.

The vocabulary was available in a table within one .doc file.

Tatoeba sentences are available in separate csv or tsv files for each language. Each sentence for each language has a unique id. To create a table with English and Spanish versions of the same sentences they had to be linked using another table provided (Links) which provides links between ids to associate sentences with their translations in all 397 languages.

I converted all files into lists of lists in Python and used SqlAlchemy to to upload the data into separate tables. This was quite a slow process as the lists contained hundreds of thousands of sentences and many millions of links between them. Here I will talk about an alternative. Finally, I used joins in SQL to find sentences that existed in both English and Spanish and link them together. The pre-processing scripts are available in the following files: .

## Python code for four services

Some issues included:

* When combining the services to work together I encountered frequent errors whenever the generated word contained special characters. This was an encoding issue which I resolved by decoding in 'latin-1'.

* Whilst most words have corresponding sentences some do not, which produced index errors. For now I decided to catch those errors and display a message that sentences for the word are yet to be added. I would like to change it to generating a different word when a sentence is not available until more sentences are added to the database but it's not essential for MVP.

## Unit testing



<img src="Images/unit-test.png" alt="unit testing results" class="center" style="width:20;">


# Evaluation

## What I would have done differently


## Possible additions and improvements



## Versions
