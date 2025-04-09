import mysql.connector
import dbconfig

db = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

cursor = db.cursor()
sql="delete from student where id = %s"
values = (2,)

cursor.execute(sql, values)

db.commit()
print("delete done")

db.close()
cursor.close()