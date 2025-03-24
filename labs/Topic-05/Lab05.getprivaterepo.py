# Second part of the lab05
# This code will get the private repository from github

import requests
import json
from config import apikeys as cfj

filename = "privaterepo.json"

url = 'https://api.github.com/repos/Jennyicano/aprivateone'

apikeys = cfj["githubkey"]
response = requests.get(url, auth = ('token', apikeys))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)