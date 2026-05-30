import pymysql
def addstudent():
    global merahaat,sql
    name=input("enter student name :".title()).title()
    subject=input("enter student subject :".title()).title()
    merahaat.execute(f"insert into student (name,subject) values('{name}','{subject}')")
    sql.commit()
    print("\nadded successfuly!!".upper())


def viwestudent():
    global merahaat,sql
    name=input("enter student name :".title()).title()
    merahaat.execute(f"select * from student where name='{name}'")
    data=merahaat.fetchall()
    print(data)
    for i in data:
        print("ID =",i[0])
        print("Name =",i[1])
        print("Subject =",i[2])
    sql.commit()

def viweAllstudent():
    global merahaat,sql
    merahaat.execute("select * from student")
    data=merahaat.fetchall()
    print(data)
    sql.commit()

def updatestudent():
    update=int(input("enter id which student data you want to change :".title()))
    name=input("enter new name :".title()).title()
    subject=input("enter new subject :".title()).title()
    merahaat.execute(f"update student set name='{name}',subject='{subject}' where id={update}")
    sql.commit()
    print("\nupdated successfuly!!")

def deletestudent():
    delete=int(input("enter id which student data you want to delete :".title()))
    merahaat.execute(f"delete from student where id={delete}")
    sql.commit()
    print("deleted successfuly!!".upper())


sql=pymysql.connect(host="localhost",user="root",password="9998",database="python_db_1")
merahaat=sql.cursor()
status=True
print("~~~~~~~~~welcom~~~~~~~~~~\n")
while status:
    menu=int(input("""
                    :MENU:
                press 1 for add student.
                press 2 for view student.
                press 3 for view all student.
                press 4 for update student.
                press 5 for delete student.
                press 6 for exit menu. 

    enter your choice = """.title()))
    if menu==1:
        addstudent()
    elif menu==2:
        viwestudent()
    elif menu==3:
        viweAllstudent()
    elif menu==4:
        updatestudent()
    elif menu==5:
        deletestudent()
    elif menu==6:
        print("\nthank you for comming~~~~".upper())
        status=False

sql.commit()