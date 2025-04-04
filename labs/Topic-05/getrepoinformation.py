# Practice: Topic 05 following along with the video of the lecture
# Get information a public repository from github
import requests
import json

# filename = "repos-public.json"
filename = "wsaa-code.json"

url = 'https://api.github.com/users/andrewbeattycourseware/repos?per_page=100'
#url = 'https://api.github.com/repos/andrewbeattycourseware/aprivateone'
url = 'https://api.github.com/repos/andrewbeattycourseware/wsaa-course-material/contents/code'

response = requests.get(url)
print (response.status_code)
repoJSON = response.json()
#print (response.json())

with  open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)