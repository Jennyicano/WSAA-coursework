# Module WSAA ATU Galway, Lecture Andrew Beatty
# Author: Jennifer Ibanez

# Assignment 3: "exchequer account (historical series)"
# Write a program that retrieves the dataset for the "exchequer account (historical series)" 
# from the CSO, and stores it into a file called "cso.json".

import requests
import json
    
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
response = requests.get(url)

# Check if the request was successful and 
# save the file cso.json in the folder data

if response.status_code == 200:
    data = response.json()
with open("data/cso.json", "w") as fp:
        json.dump(data, fp)
        print("Data written to cso.json")


# References:
# Python's Requests (https://realpython.com/python-requests/)
# HTTP response status codes (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
# HTTP general information (https://www.jmarshall.com/easy/http/)
