from datetime import datetime as d,timedelta as t
import json as j
import os

obb=d.now()
print(obb)

os.chdir(os.getcwd()+"\\vaccination report")
mi=obb+t(minutes=1)
while 1:
    print(obb.time())
    if mi.time()==obb.time():
        break
# mi=obb+t(minutes=1)
# print(mi)
# if mi.time():
#     data={}
#     data['name']=input("enter your name :")
#     data['age']=int(input("enetr your age :"))
#     with open(f"{obb.time}.json",'w') as f:
#         j.dump(data,f,indent=4)