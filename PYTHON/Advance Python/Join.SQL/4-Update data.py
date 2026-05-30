import pymysql
sql=pymysql.connect(host="localhost",user="root",password="9998",database="python_db_1")
haat=sql.cursor()
name="boss"
subject="java"
haat.execute(f"update student set name='{name}',subject='{subject}' where id=2")
sql.commit()