# PurBeurre

## Introduction

The french Startup Pur Beurre is known for French food habits. Their restaurant, Ratatouille, is becoming increasingly popular and is attracting more visitors to the Montmartre hill.

The team noticed that their users wanted to change their diet but did not know where to start. Replace Nutella with hazelnut paste, yes, but which one? And in which store to buy it? Their idea is to create a program that would interact with the Open Food Facts database to retrieve food, compare it and offer the user a healthier substitute for the food that makes him want.

## Specifications

### Description of the user journey

The user is on the terminal. The latter shows him the following choices:

1. Which food do you want to replace?
2. Find my substituted foods.

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
* [ ] Write a Python function to create the tables in the database
* [ ] Retrieve data in json format via OpenFoodFacts API
* [ ] Insert data collected from the API into your database
* [ ] Build the program _(menu, question / answer system ...)_
* [ ] Saving user search results to the database

---
> 2018 - OpenClassrooms - Project 05
