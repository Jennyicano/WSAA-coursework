import mysql.connector
import dbconfig

db = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

cursor = db.cursor()
sql="update student set name= %s, age=%s  where id = %s"
values = ("Joe",33, 1)

cursor.execute(sql, values)

db.commit()
print("update done")

cursor.close()
db.close()