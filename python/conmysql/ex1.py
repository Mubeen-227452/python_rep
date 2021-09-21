import mysql.connector

import conf1

print(conf1.host)
db1 = mysql.connector.connect(host=conf1.host, username=conf1.username, password=conf1.password,
                              database=conf1.database)
cur = db1.cursor()
cur.execute("select * from cus")
res = cur.fetchall()
for i in res:
    print(i)
