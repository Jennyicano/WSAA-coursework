# Practice following the lesson 3.1

import requests
import json
# this is flakey at the moment
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
#with open("bitcoindump.json", "w") as fp:
#    json.dump(data, fp)

euroobject = data["bpi"]["EUR"]
rate = euroobject["rate"]
print(rate)