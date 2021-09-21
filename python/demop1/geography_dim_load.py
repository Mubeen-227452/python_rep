import mysql.connector
import conf1

db3 = mysql.connector.connect(host="localhost", username="root", password="7894", database="testp1")
cur2 = db3.cursor()
cur2.execute("select * from geography")
data_from_geography = cur2.fetchall()
res = list(list(sub) for sub in data_from_geography)
print(data_from_geography)
print(res)

q = "insert into geography_dim(geography_id,geography_name) select * from geography on duplicate key update  \
    geography_id=VALUES(geography_id),geography_name=VALUES(geography_name) "
cur2.execute(q)
db3.commit()
