import mysql.connector
import MySQLdb

db2 = mysql.connector.connect(host="localhost", username="root", password="7894", database="testp1")
cur1 = db2.cursor()
for line  in open('exp.txt', 'r') :

    items = line.split('|')  # strip new-line characters and split on column delimiter
    values = [item.strip() for item in items]
    query = "INSERT INTO dept VALUES (%s,%s)"
    cur1.executemany(query, (values,))

db2.commit()