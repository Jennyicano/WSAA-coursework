# Module WSAA ATU Galway, Lecturer Andrew Beatty
# Author: Jennifer Ibanez

# Assignment 2: Card Draw
# Write a program that simulates a deck of cards and deals (print out) 5 cards.
# Then if the user has drawn a pair, triple, straight, or all of the same suit congratulate the user.
# For this assignment I'll use the [Desk of Cards API](https://deckofcardsapi.com/)

import requests
import json

# First I'll need a new deck of cards and shuffle them
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
data = response.json()
print(data) # To check it works and it's doing the shuffle
# Store data in a json file
with open ("deck.json", "w") as fp:
    json.dump(data, fp)

# I'll print the deck_id to check it work
deck_id = data["deck_id"]
print(deck_id)

# Now I'll draw 5 cards from the deck
url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(url)
data = response.json()
print(data) # To check it works and it's drawing the cards

# Store data in a json file
with open ("cards.json", "w") as fp:
    json.dump(data, fp)

# If the user has drawn a pair, triple, straight, or all of the same suit congratulate the user.

cards = data["cards"]
values = []
for card in cards:
    values.append(card["value"])
    # Adding the values to the list.
    if values.count(card["value"]) == 2:
        print("Congratulations! You have drawn a pair!")
    if values.count(card["value"]) == 3:
        print("Congratulations! You have drawn a triple!")
    if values.count(card["value"]) == 4:
        print("Congratulations! You have drawn a straight!")
    if values.count(card["value"]) == 5:
        print("Congratulations! You have drawn all of the same suit!") 
print(values)

# It's giving error when I try to run the code, I'll try to fix it later.