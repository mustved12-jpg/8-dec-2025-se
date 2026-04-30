import json
l1=[]
no=int(input("enter howe many data you wanted to add :".title()))
for i in range(no):
    d={}
    d['id']=int(input("enetr your id :".upper()))
    d['name']=input("enetr your name :".upper()).title()
    d['subject']=input("enetr your subject :".upper()).title()
    d['score']=float(input('enetr your score :'.upper()))
    l1.append(d)

with open('json 2.json','w') as f:
    json.dump(l1,f,indent=4)
print("data added successfuly!.")