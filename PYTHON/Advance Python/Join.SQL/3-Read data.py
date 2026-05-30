import pymysql

sql=pymysql.connect(host="localhost",user="root",password="9998",database="python_db_1")
haat=sql.cursor()
name=input("enter witch student details you want :")#mustved
query="select*from student where name='%s'"
haat.execute(query%name)
data=haat.fetchall()
print(data)#((1, 'mustved', 'python'),) ese ayega output
sql.commit()

#               OR aasan vala

sql=pymysql.connect(host="localhost",user="root",password="9998",database="python_db_1")
haat=sql.cursor()
name=input("enter witch student details you want :")#mustved
haat.execute(f"select*from student where name='{name}'")
data=haat.fetchall()
print(data)#((1, 'mustved', 'python'),) ese ayega output
sql.commit()



# all data
sql=pymysql.connect(host="localhost",user="root",password="9998",database="python_db_1")
haat=sql.cursor()
haat.execute("select * from student")
data=haat.fetchall()
print(data)#((1, 'mustved', 'python'), (2, 'ok', 'j')) ese ayega output
sql.commit()


for i in data:
    print("ID =",i[0])
    print("Name =",i[1])
    print("subject =",i[2])


