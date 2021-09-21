import csv

import mysql.connector
import conf1

"""
db3 = mysql.connector.connect(host=conf1.host, username=conf1.username, password=conf1.password, database=conf1.database)
cur2 = db3.cursor()
f_n= "emp"
with open("C:/Users/mubee/OneDrive/Desktop/Book1.csv", "r") as file:
    lines = file.readlines()[1:]
    lines = [item.strip().split(',') for item in lines]
    print(lines)
sql = "insert ignore into cus values (%s, %s, %s, %s, %s)"
cur2.executemany(sql, lines)
##cur2.execute("delete from emp where empname='val2'")
db3.commit()
cur2.close()
db3.close()"""


def Load_data(filename,delim):
    print(filename)
    db3 = mysql.connector.connect(host=conf1.host, username=conf1.username, password=conf1.password,
                                  database=conf1.database)
    cur2 = db3.cursor()
    with open(f"D:/datas/{filename}.csv")as file:
        lines = file.readlines()[1:]
        lines = [item.strip().split(delim) for item in lines]
        print(lines)

    str1 = ""
    for i in range(0, len(lines[0])):
        str1 += "%s,"
    str1 = str1[:-1]

    print(str1)
    sql = f"insert ignore  into {filename} values ({str1})"
    cur2.executemany(sql, lines)
    db3.commit()

##Load_data("D:/datas/empp",",")

f = open("D:/datas/tables.txt")
name = f.readlines()
name = [i.strip() for i in name]
print(name)

for y in name:
    Load_data(y,",")
