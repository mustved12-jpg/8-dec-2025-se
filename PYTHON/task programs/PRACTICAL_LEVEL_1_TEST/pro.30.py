#Q 30: Write a function that accepts a list of strings and returns the total number of characters in all strings.
l1=['java','python','php','android','flutter','java']
d={}
for i in l1:
    if i not in d:
        d[i]={}
    for j in i:
        if j not in d[i]:
            d[i][j]=1
        else:
            d[i][j]+=1
for k1,v1 in d.items():
    print(k1,end=" = ")
    for k,v in v1.items():
        print(f"{k}:{v}",end=", ")
    print()