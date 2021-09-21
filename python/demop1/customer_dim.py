import mysql.connector
import conf1

db3 = mysql.connector.connect(host="localhost", username="root", password="7894", database="testp1")
cur2 = db3.cursor()

q = "insert into customer_dim(cust_fname,cust_mname,cust_lname,cust_ssn,cust_stname,cust_city,cust_state,cust_country,cust_zip,cust_phone,cust_email)\
    select initcap(f_name)as f_name,lower(m_name)as m_name,initcap(l_name) as l_name,cast(ssn as decimal),\
    concat(apt_no,',',st_name),city,state,country,cast(zip as decimal),\
    cast(concat(left(phone,3),'-',mid(phone,4,3),'-',right(phone,4))as char)as phone,email from customer\
    where not exists(select * from customer_dim  where(customer.ssn=customer_dim.cust_ssn and  \
    initcap(customer.f_name)=customer_dim.cust_fname and lower(customer.m_name)=customer_dim.cust_mname and \
    initcap(customer.l_name)=customer_dim.cust_lname  and \
    concat(customer.apt_no,',',customer.st_name)=customer_dim.cust_stname and\
    customer.city=customer_dim.cust_city and \
    customer.state=customer_dim.cust_state and \
    customer.country=customer_dim.cust_country and \
     cast(concat(left(customer.phone,3),'-',mid(customer.phone,4,3),'-',right(customer.phone,4))as char)=customer_dim.cust_phone and \
     customer.email=customer_dim.cust_email))  "
cur2.execute(q)
db3.commit()
