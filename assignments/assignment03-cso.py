# Module WSAA ATU Galway, Lecture Andrew Beatty
# Author: Jennifer Ibanez

# Assignment 3: Card Draw
# Write a program that retrieves the dataset for the "exchequer account (historical series)" 
# from the CSO, and stores it into a file called "cso.json".

import requests
import json
    
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("Data retrieved successfully")

    def get_all():
        with open("cso.json", "w") as fp:
            json.dump(data, fp)
            print("Data written to cso.json")
            return data

    get_all()
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    
