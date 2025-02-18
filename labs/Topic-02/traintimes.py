# Lab topic 2:
# Write a program that prints the data for all trains in Ireland to the console

import requests
import csv
from xml.dom.minidom import parseString 

# parseString is a function in the minidom module

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

# check it works
print (doc.toprettyxml()) # output to console comment this out once you know it works

# to store the xml in a file
with open("trains.xml", "w") as xmlfp:
    doc.writexml(xmlfp)

# make an array called retrieveTags that will store all the names of the tags that we want to retrieve.  
retrieveTags=['TrainStatus',
              'TrainLatitude',
              'TrainLongitude',
              'TrainCode',
              'TrainDate',
              'PublicMessage',
              'Direction'
              ]
# Modify the program to print out each of the trainscodes.
    # objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    # for objTrainPositionsNode in objTrainPositionsNodes:
        # traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        # traincode = traincodenode.firstChild.nodeValue.strip()
    # print (traincode)

# adding the newline= '' parameter 

with  open('week02_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        
# get everything in a list
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        
        # write the list to the csv file
        train_writer.writerow(dataList)
        
# Store only the trains whose TrainCode starts with a D
        if dataList[3].startswith('D'):
            print(dataList)
            train_writer.writerow(dataList)
