# import pymysql

# def addstudent():
#     name=input("enter your name :")
#     subject=input("enter your subject :")
#     score=float(input("enter your score :"))
#     city=input("enter your city name :")
#     enter="""insert into student(name,subject,score,city)values('%s','%s',%s,'%s')"""
#     args=(name,subject,score,city)
#     haat.execute(enter % args)
#     sql.commit()

    
# sql=pymysql.connect(host="localhost",user="root",password="9998102762",database="python_db_1")
# # haat.execute("alter table student add city varchar(20)")

# haat=sql.cursor()
# addstudent()
import pymysql

sql=pymysql.connect(host="localhost",user="root",password="9998")
haat=sql.cursor()
haat.execute("create database if not exists python_db_1")
sql.commit()

sql=pymysql.connect(host="localhost",user="root",password="9998",database="python_db_1")
haat=sql.cursor()
haat.execute("create table if not exists student(id int auto_increment\
     primary key,name text,subject varchar(20) default 'Python')")

name=input("enter your name :")
subject=input("enter your subject :")
query="insert into student (name,subject) values('%s','%s')"
args=(name,subject)
haat.execute(query % args)
sql.commit()