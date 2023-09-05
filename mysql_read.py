print('Mysql')

import mysql.connector

dbconnection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    database = 'pythondb'
)

mycursor = dbconnection.cursor() #Start automatisch aan het begin
mycursor.execute('SELECT * FROM persons')
#Alle data ophalen met
alleregels = mycursor.fetchall()