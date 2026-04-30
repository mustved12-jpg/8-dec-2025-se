import csv
data=[
    ['sr.no','name','subject'],"\n",#iske bad ek new line bnegi
    [1,'mustved','python'],
    [2,'aaa','java'],
    [3,'bbb','php']
]
with open('csv 1.csv','w',newline="") as f:# new line nhi likhen ge to ek extra line aye gi 
    # obj=csv.writer(f)
    # obj.writerows(data)
    csv.writer(f).writerows(data)
    