import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
mycursor = mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)


mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="demodb")
mycursor = mydb.cursor()
mycursor.execute("select * from test")
result = mycursor.fetchone()
for i in result:
    print(i)

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
mycursor = mydb.cursor()
mycursor.execute("insert into test ")
result = mycursor.fetchone()
for i in result:
    print(i)