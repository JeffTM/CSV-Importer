import mysql.connector
from mysql.connector import connect as mysql_connect

host = input("Host: ")
if not host:
    host = 'localhost'
    print('Using localhost')
username = input("Username: ")
password = input("Password: ")

try:
    conn = mysql_connect(host = host, user = username, passwd = password, auth_plugin='mysql_native_password')
except mysql.connector.errors.DatabaseError as e:
    print('Error: could not connect to database')
    print(e)
else:
    print('Connected to database')

