# Practice following the topic 2.4 from the course videos.
# Reading json from a file

import json
filename = "2.4-json.json"

with open(filename, "r") as fp:
    jsonobject = json.load(fp)
#print (jsonobject)
for employee in jsonobject["employees"]:
    print(employee["firstName"])
