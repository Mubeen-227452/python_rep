import mysql.connector
import conf1


def Load_data(filename, deli):
    db3 = mysql.connector.connect(host=conf1.host, username=conf1.username, password=conf1.password,
                                  database=conf1.database)
    cur2 = db3.cursor()
    file = open(f"{filename}.txt")
    colum = file.readline()
    cl = colum.strip().split(deli)
    c =  ""
    for i in cl:
        c += i+","
    c = c[:-1]
    print(c)
    lines = file.readlines()[1:]
    lines = [item.strip().split(deli) for item in lines]
    print(lines)
    str1 = ""
    for i in range(0, len(lines[0])):
        str1 += "%s,"
    str1 = str1[:-1]
    str2 = ""
    for i in range(0,len(lines[0])):
        str2 += "col"+str(i+1)+","
    str2 = str2[:-1]
    print(str2)
    sql = f"insert ignore into {filename}   values ({str1})"
    cur2.executemany(sql, lines)
    ##cur2.execute("delete from emp where empname='val2'")
    db3.commit()
    cur2.close()
    db3.close()


##Load_data("emp", "|")

f = open("table.txt")
name = f.readlines()
name = [i.strip() for i in name]
print(name)

for y in name:
    Load_data(y,"|")

