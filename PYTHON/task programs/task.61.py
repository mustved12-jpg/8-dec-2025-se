import copy

l1=[1,2,3,[10,20],4,5]
l2=copy.deepcopy(l1)#agar me ye nhi likhunga to [3][0] dono me chang hoga
l2[0]=10
l2[3][0]=100
print(f"{l1}\n{l2}")
# sem dictionryme bhi hota hai
d={1:10,2:{20:200}}
d1=d
d1[1]=100# ye dono me chang ho jayega q ki mene nahi copy kiya ho nahi deepcopy
print(f"{d}\n{d1}")


print(f"{id(l1)}\n{id(l2)}")
print(f"{id(d)}\n{id(d1)}")