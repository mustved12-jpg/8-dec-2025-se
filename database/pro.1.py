from pymysql.cursors import Cursor
import pymysql
import pymysql
Con=pymysql.connect(host="localhost",user="root",passwd="9998102762")

Cursor=Con.cursor()
Cursor.execute("create database if not exists python_db_practice")
Con.commit()

Con=pymysql.connect(host="localhost",user="root",passwd="9998102762",database="python_db_practice")

# Cursor=Con.cursor()
# Cursor.execute("create database if not exists python_db_practice")
# Con.commit()

Cursor.execute("create table if not exists student (id int auto_increment,name varchar(20),subject varchar(20),score int)")
Con.commit()
# Con=pymysql.connect(host="localhost",user="root",passwd="9998102762",database="python_db_practice")
# Cursor=Con.cursor()

# Cursor=Con.cursor()

# def Add():
#     name=input("enter your name:")
#     sub=input("enter your subject :")
#     score=int(input("enter your score :"))
    
    