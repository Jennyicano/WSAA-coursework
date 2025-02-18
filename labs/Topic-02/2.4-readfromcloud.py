# examples following lesson 2.4
# Reading json from the cloud (json in the wild)

import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
#print (response.json())
data = response.json()
#with open ("bitcoindump.json", "w") as fp:
#json.dump(data, fp)

bpi = data["bpi"]
#print(bpi)
rate = bpi["USD"]["rate"]
print(rate)