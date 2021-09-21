import csv

f = open("example.csv","r")
rdr = csv.reader(f, delimiter=",")
print(rdr)
for row in rdr:
    print(row[0])
f.close()
