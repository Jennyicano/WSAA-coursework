# Module WSAA ATU Galway, Lecturer Andrew Beatty
# Author: Jennifer Ibanez

# Assignment 2: Card Draw
# Write a program that simulates a deck of cards and deals (print out) 5 cards.
# Then if the user has drawn a pair, triple, straight, or all of the same suit congratulate the user.
# For this assignment I'll use the Desk of Cards API: https://deckofcardsapi.com/

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

# I'll print the deck_id to check it works
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
#["10","K","Q","J","A"]
suits = []
#[hearts,hearts,h,h,diamonds]

# I created 2 arrays, one for the values and one for the suits

for card in cards:
    values.append(card["value"])
    suits.append(card["suit"])
    
# print(values)
# print(suits)

equalSuits = False
# suits= [1,1,1,1,1] to check if all the suits are the same
# for all the cards the same suit

def check_suits(suits):
    # for all the cards the same suit
    return (suits.count(suits[0])==len(suits))

# takes the first element (suits[0]) of the list suits and counts how many times it appears in the list suits
# if the count is equal to the length of the list suits, then all the suits are the same
equalSuits = check_suits(suits)
if equalSuits:
    print("Congratulations all the cards have the same suit")

def pair(values):
    # for a pair
    return len(set(values)) == 4

# I'll check for pair, triples or 4 cards with the same value
# values = []
check_other_pair=False
# I'll check if there is a second pair in the list
print("values" , values)
maximo = max(values, key=values.count) 
# I'll give the value maximo to the card value that appears the most in the list
print("max.count", values.count(maximo))
print("maximo", maximo)
if values.count(maximo) == 4:
    print("Congratulations you have 4 cards with the same value")
elif values.count(maximo) == 3:
    print("Congratulations you have 3 cards with the same value ", maximo)
    check_other_pair=True # I'll check if there is a second pair in the list
elif values.count(maximo) == 2:
    print("Congratulations you have a pair, the value is ", maximo)
    check_other_pair=True # I'll check if there is a second pair in the list
else:
    print("Try again") 

if check_other_pair:
    values2= values.copy()
    values2.sort()
    # print("values2", values2)
    indices = [i for i, x in enumerate(values2) if x == maximo]
    # print("indices", indices)
    del values2[indices[0]:indices[-1]+1]
    # print("values2", values2)
    maximo2 = max(values2, key=values2.count) 
    # print("maximo2", maximo2)
    if values2.count(maximo2) == 2:
        print("Congratulations you have a pair, the value is ", maximo2)

# The next step it's to check for a straight hand
# I'll create a dictionary with the values of the cards, giving the name of the cards as Jack, Queen, King and Ace
# the values 11, 12, 13 and 1 respectively.
values_dict = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"JACK":11,"QUEEN":12,"KING":13,"ACE":1}
# I'll create a list with the values of the cards
values_list = [values_dict[value] for value in values]
values_list.sort()
# Congratulate the user if the values of the cards are consecutive and have a straight
if values_list == list(range(values_list[0], values_list[-1]+1)):
    print("Congratulations you have a straight")


   