d={"student":{'name':'boos','subject':'java','id':1}}
# l1=[1,1,2,2,3,3]
def my(k,**ok):
    global d
    print(k)
    print(ok)
    print(d[k]["name"])
    for i in ok.keys():
        key=i
        break
    d[k][key]="mustved"

print(d)
# my(1010,**d["student"])

for k,v in d.items():
    my(k,**v)
print(d)

