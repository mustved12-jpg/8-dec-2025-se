import pymysql
sql=pymysql.connect(host="localhost",user="root",password="9998")
haat=sql.cursor()
haat.execute("create database if not exists python_db_1")
sql.commit()


sql=pymysql.connect(host="localhost",user="root",password="9998",database="python_db_1")
haat=sql.cursor()
haat.execute("create table if not exists student(id int primary key auto_increment,name text,subject varchar(20) default 'python',score float)")
sql.commit()
