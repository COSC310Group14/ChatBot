# Project Description
The goal of the project is to create an interactive conversational agent that assumes the role of a Psychiatrist.The Chatbot will essentially output *canned* responses to a users input. More specifically the bot will be trained to deal with users that are dealing with a variety of emotions such as depression, stress, loneliness. The user in this case will be a patients seeking help. 

## Chosen SDLC
The Software Development Lifecycle that we chose is the agile method. This model allows us to test and debug more due to the short iterations. It also allows us to identify problems and risks earlier and prevent them from happening in the future. Moreover, it provides us with flexibility to change things as we develop the chat bot, certain features or requirements.

## Limitations

•	The code is limited by the NLP algorithm which aims to understand what the user is writing and provide an answer from a json file with possible answers. Therefore, the bot is limited by the size and complexity of the provided responses. 

•	Since the bot is following a predetermined structure the same answer can be provided to the user repetitively. 


## Installation and Setup 

In order to run the chat bot the user must install the following libraries nltk, numpy, tflearn,random, json, pickle, tkinter, nltk. 

## Machine Learning
todo

## Synonym Recognition
Synonyms are used to improve upon the accuracy of the chatbot. By adding the synonyms one can answer the questions asked by the user that don’t really match the questions fed by you. This way, the bot can identify the intent and provide the right answer even when the question asked is not an exact match. For example if the user enters " I am feeling gloomy", the bot is not hardcoded to find the word gloomy and relate it to depression, but the synonym recognition script will find all the synonyms of gloomy and iterate through those synonimous phrases until it can understand something. In this case the phrase understood by the bot would be " I am feeling depressed".

The synonym recognition is done via the nltk + the WordNet toolkit. The script runs synonym recognition for each word in the string and generates a list of synonimous phrases.
Source: https://wordnet.princeton.edu/
