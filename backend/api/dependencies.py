import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="myuser",
    password="mypassword",
    database="mydatabase"
)
