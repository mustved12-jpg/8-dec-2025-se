li=[f"{i},even" if i%2==0 else (i,"odd") for i in range(1,8)]
print(li)

l1=[]
for i in range(1,6):
    name=input(f"enter your {i}name:").upper()
    l1.append(name)
print(l1)

l2=[i if i>2 else f"{i} number is greter then 2" for i in range(1,6)]
print(l2)
