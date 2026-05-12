from datetime import datetime as d,timedelta as t
import json as j
import os

# os.mkdir("vaccination report")
os.chdir(os.getcwd()+"\\vaccination report")
tim_e=d.now().date()
l1=[]

while 1:
    d={}
    d['Name']=input("enter your name :".upper()).title()
    contact_No=int(input("enter your contact number :".upper()))
    if contact_No>1000000000 and contact_No<10000000000:
        d['Contact No']=contact_No
    else:
        d['Contact No']=None
    d['Age']=int(input("enter your age :".upper()))
    d['Gender']=input('enter your gender :'.upper()).upper()
    d['vaccine name'.title()]=input('enter vaccine name :'.upper()).title()
    with open(f"{tim_e}.txt",'a') as f1:
            f1.write(f"{d},\n")
    l1.append(d)
    ch=input("do you van to add more data press y/n :".upper()).upper()
    if ch=="Y":
        continue
    else:
        break
if os.path.exists(f"json {tim_e}.json"):
    with open(f"json {tim_e}.json",'r') as f:
        data=j.load(f)
    for i in range(len(data)):
        l1.insert(i,data[i])
with open(f"json {tim_e}.json",'w') as f:
    j.dump(l1,f,indent=4)