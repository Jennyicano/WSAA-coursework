# Steps to create a database and a table using python
# Install packages
# pip install mysql-connector

import mysql.connector

dn = mysql.connector.connect(
    host="localhost",
    user='root',
    password="",
    port=3306,
)

cursor = db.cursor()

# Create a database
cursor.execute("Create DATABASE wsaa")

db.close()
cursor.close()
 