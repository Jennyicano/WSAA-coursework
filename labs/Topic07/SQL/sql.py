# How to connect to a database and execute SQL queries

import mysql.connector

# Connect to the database
mydb = mysqul.connector.connect(
    host="localhost",
    user="????",
    password="????",
    database="????"
)
# Create a cursor object
mycursor = mydb.cursor()
sql="some sql"
mycursor.execute(sql)

# commit if create, update or delete
mycursor.close()
mydb.close()

