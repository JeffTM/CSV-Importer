import mysql.connector
from mysql.connector import connect as mysql_connect

#Get connection info
host = input("Host: ")
if not host:
    host = 'localhost'
    print('Using localhost')
username = input("Username: ")
password = input("Password: ")
database = input("Database: ")

#Connect to the database and create a cursor
try:
    conn = mysql_connect(host = host,
                         user = username,
                         passwd = password,
                         database = database,
                         auth_plugin='mysql_native_password')
    cursor = conn.cursor()
except mysql.connector.errors.DatabaseError as e:
    print('Error: could not connect to the database')
    print(e)
else:
    print('Connected to database')

#Get the file

#Get table info
table_name = input("Table name: ")
