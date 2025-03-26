# Module WSAA ATU Galway, Lecture Andrew Beatty
# Author: Jennifer Ibanez

# Assignment 4: Write a program in python that will read a file from a repository, 
# The program should then replace all the instances of the text "Andrew" with your name. 
# The program should then commit those changes and push the file back to the repository 

# pip install requests
import pip 
from github import Github
import requests
from config import apikeys as cfj

# Modify the program to get the clone URL of a repository on your account 
# m(you could make a private one just for this if you wish). 
# Put a file in the repository called test.txt

# Apykey 
apikeys = cfj["githubkey"]
g = Github(apikeys)

repo = g.get_repo("Jennyicano/aprivateone")
print(repo.clone_url)

# Get the download URL of the file in this repository called test.txt 

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
# print(urlOfFile)

# Use the download URL to make a http request to the file can output the contents of the file
response = requests.get(urlOfFile)
contentOfFile = response.text
# print (contentOfFile)

# Append the text more stuff (with a newline character) to the contents of the file
newContents = contentOfFile.replace('Andrew', 'Jenny')
print(newContents)

# Update the contents of the file 

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)
print(gitHubResponse)

# Push the changes to the repository
# Look at the file on GitHub and confirm that the text was added

# Saving the file in this repository called test.txt in the folder data.

save = open("data/test.txt", "w")
save.write(newContents)
save.close()