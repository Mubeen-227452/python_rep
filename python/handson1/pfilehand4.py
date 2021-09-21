import mysql.connector

db1 = mysql.connector.connect(host="localhost", username="root", password="7894", database="testp1")
cur = db1.cursor()

file = open("exp.txt", "r")
lines = file.readlines()[1:]
lines = [item.strip().split('|') for item in lines]
sql = "insert into dept values (%s, %s)"
cur.executemany(sql,lines)
db1.commit()
