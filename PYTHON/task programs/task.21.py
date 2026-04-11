'''
l1=['java', 'python', 'php', 'android', 'flutter']
l2=[]
print(l1.find("python"))        //baki hai 
for i in l1:
    i=i.replace(i,i[::-1])
    pass
print(l1)
print(l2)'''
s1="278136 ashdbhaksd 382"
print(s1)
sume=""
num=""
co=0
for i in range(len(s1)):
    if s1[i]>="0" and s1[i]<="9":
        print(s1[i])
        sume+=s1[i]
    else:
        if s1[i]==" ":
            co+=1
        else:
            num+=s1[i] 

num=num.strip()
print(sume)
print(num)

l1="278136 ashdbhaksd 382"
l1=l1.split()
print(l1)
num=""
for i in l1:
    if i.isalpha():
        continue
    else:
        num+=i+" "

print(num)