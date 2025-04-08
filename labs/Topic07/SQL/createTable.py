#How to create a table in a database using python

import mysql.connector
import dbconfig

db = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

cursor = db.cursor()
sql="CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(250), age INT)"

cursor.execute(sql)

db.close()
cursor.close()