import mysql.connector
import conf1


def lt(filename, deli):
    try:
        db3 = mysql.connector.connect(host=conf1.host, username=conf1.username, password=conf1.password,
                                      database=conf1.database)
        cur2 = db3.cursor()
        f_n = "emp"
        file = open(f"{filename}.txt")
        cl = file.readline()
        cl = cl.strip().split(deli)
        c = ""
        d = ""
        s = ""
        for i in cl:
            s += "%s,"
            c += i + ","
            d += i + "=" + "VALUES" + "(" + i + ")" + ","
        s = s[:-1]
        c = c[:-1]
        d = d[:-1]

        print(c)
        print(s)
        print(d)
        print(cl)
        """
        d = ""
        for y in cl:
            d +=y+"="+"VALUES"+"("+y+")"+","
        d=d[:-1]
        print(d)"""

        l = file.readlines()[:]
        l = [item.strip().split(deli) for item in l]
        # lines = res = list(tuple(sub) for sub in l)
        print(l)
        print(type(l))

        sql = f"\
            insert  into {filename}({c}) VALUES ({s})\
              ON DUPLICATE  KEY UPDATE  {d} "

        cur2.executemany(sql, l)
        ##cur2.execute("delete from emp where empname='val2'")
        db3.commit()
        print(f"Record inserted successfully into {filename} table")
    except mysql.connector.Error as error:
        print(f"Failed to insert into MySQL table {filename}".format(error))
    except FileNotFoundError as error1:
        print(f"File not found {filename}".format(error1))
    finally:
        if db3.is_connected():
            cur2.close()
            db3.close()
            print("MySQL connection is closed")


lt("geography", "|")
lt("customer","|")
"""
f = open("table.txt")
name = f.readlines()
name = [i.strip() for i in name]
print(name)

for y in name:
    lt(y, "|")
"""
