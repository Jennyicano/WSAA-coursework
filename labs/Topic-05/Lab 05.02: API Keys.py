# In this lab we are going to use Python access APIs that need a key
# This lab follows the lectures on APIs topic 5
# Author Jennifer Ibanez cano

import requests
import urllib.parse
import json
from config import apikeys as cfj

targetUrl = "https://en.wikipedia.org"

apiKeys = cfj["html2pdf"]

apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'html': targetUrl,'apiKey': apiKeys}
parsedparams = urllib.parse.urlencode(params)

requestUrl = apiurl +"?" + parsedparams

response = requests.get(requestUrl)

print (response.status_code)

result =response.content
with open("document.pdf", "wb") as handler:
    handler.write(result)
    
# The PDF file is saved in the same folder as the script but it's very big