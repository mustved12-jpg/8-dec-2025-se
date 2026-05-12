import csv
l1=['name','score','subject','id']
d={'name':'mustved','score':65,'subject':'python'}
with open("csv 2.csv",'w',newline="") as f:
    csv.writer(f).writerows(d.items())
    f.write('\n')#new line ke liye 
#--------------------------------data collection type ke form me hi jata hai direct nhi jata
with open("csv 2.csv",'a',newline="") as f:
    csv.writer(f).writerow(l1)# ek ek line kar ke add kre ga
    csv.writer(f).writerow(['mustved',54,'python',3])# ye dusri line hai