import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cmrec@1234",database="mydb")
mycurs = mydb.cursor()
#mycurs.execute("create database mydb")
#mycurs.execute("SHOW DATABASES")
#mycurs.execute("create table users( name varchar(50), email varchar(50), password varchar(50))")
mycurs.execute("select * from users")
#sql="Insert into users(name,email,password)values(%s,%s,%s)"
#val=("mercy","mercy@gmail.com","cmrec")
#mycurs.execute(sql,val)
#mycurs.execute("show tables")
#for db in mycurs:
  #  print(db)