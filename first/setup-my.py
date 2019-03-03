import mysql.connector

mydb = mysql.connector.connect(
    host="http://localhost",
    user="root",
    passwd=""
)

print(mydb)
