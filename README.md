# PurBeurre

## Introduction

The french Startup Pur Beurre is known for French food habits. Their restaurant, Ratatouille, is becoming increasingly popular and is attracting more visitors to the Montmartre hill.

The team noticed that their users wanted to change their diet but did not know where to start. Replace Nutella with hazelnut paste, yes, but which one? And in which store to buy it? Their idea is to create a program that would interact with the Open Food Facts database to retrieve food, compare it and offer the user a healthier substitute for the food that makes him want.

## Installation

**Important:** Requires '`Python3`'.

**For information:** This program uses the following modules:

* '`requests`',
* '`colorama`' ,
* '`mysql-connector`'.

First clone repository, in command prompt or terminal, enter this:

```console
git clone "https://github.com/vincenthouillon/purbeurre"
```

Create the PURBEURRE database by running `create_dbase.sql`.

This script creates the "Purbeurre" database and the "records" table with user access for the program.

 ```console
 mysql -u root -p 
 Enter password: [your password]
 ```

Finally, open the command prompt in the folder you just cloned and enter this:

```console
python -m venv venv
python venv/Scripts/activate
pip install -r requirements.txt
purbeurre.py
```

For disable the virtal environnement, enter:

```console
deactivate
```

## Specifications

### Description of the user journey

The user is on the terminal. The latter shows him the following choices:

1. Quel aliment souhaitez-vous remplacer ?
2. Retrouver mes aliments substitués.

The user selects 1. The program asks the user the following questions and the user selects the answers:

* Select the category. _(Several proposals associated with a number. The user enters the corresponding digit and presses enter)_
* Select the food. _(Several proposals associated with a number. The user enters the digit corresponding to the selected food and presses enter)_
* The program offers a substitute, its description, a store or buy it _(if any)_ and a link to the Open Food Facts page regarding this food.
* The user then has the possibility to save the result in the database.

## Roadmap

* [x] Cut your program into "user stories" then into tasks and subtasks and create an "agile" table _(Using Trello)_
* [x] Initialize a GitHub Repo
* [x] Start writing the documentation
* [x] Write a Python function to create the database
* [x] Write a Python function to create the tables in the database
* [x] Retrieve data in json format via OpenFoodFacts API
* [x] Build the program _(menu, question / answer system ...)_
* [x] Saving user search results to the database
* [x] Insert data collected from the API into your database

---
> 2018 - OpenClassrooms - Project 05
