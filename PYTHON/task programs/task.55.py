import json
import csv
import os
with open("heelooo boss","a") as f:
    f.write("\nimmmm mustved")
d={'name':"mustved",'id':1,"subject":'python'}
with open("file json.json","w")as f:
    json.dump(d,f,indent=4)

with open("file json.json","r")as f:
    data=json.load(f)
print(data)

l1=[['id','name','subject'],
     [f"{1}\t",'mustved','python'],
     [2,'aaaa','java'],
     [3,'bbbb','pjp']]
with open("file.csv","w",newline="") as f:
    csv.writer(f).writerows(l1)