#How to insert data into the tables in the database using python

import mysql.connector
import dbconfig

db = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

cursor = db.cursor()
sql="insert into student (name, age) values (%s,%s)"
values = ("Paqui",25)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()