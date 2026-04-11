li=[113,13,2,32,43,"python",67,78,975,943,23,8]
e=[]
o=[]
print(li)
for i in li:
    if type(i)==str:
        continue
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
        
print(e)
print(o)
#print(type(li[5]))