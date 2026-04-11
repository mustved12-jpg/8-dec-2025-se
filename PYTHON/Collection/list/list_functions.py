li=[22,93,84,3,132,-1000,434,53,62,3,34,61,True,34,14,23,32,5,65,1,0,2,7]
print(li)
print("maximum in list =",max(li))
print("minimum in list =",min(li))
print("addition all number =",sum(li))
#{max,min,sum =tabhi hoga jun listme khali numbers honge agar string huva to nhi hoga.}


li=[22,93,84,"java",3,132,-103,61,True,34,14,"python",32,5,65,1,0,2,7]
print(li)
li.reverse()
print(li)

li=[22,93,84,3,132,-1000,434,53,62,3,34,61,True,34,14,23,32,5,65,1,0,2,7]
print(li)

li.sort()#ascending order me kare ga but agar string hui to erorr hogi

print(li)

li.sort(reverse=True)# descending orde sem no string 
print(li)
li=[22,93,84,3,132,-1000,434,53,62,3,34,61,True,34,14,23,32,5,65,1,0,2,7]
#method
print("count 3 kitni bar hai =",li.count(3))
print("find 3 ka index =",li.index(3,+4))
# index ko samjhne ke liye string me pro.3 dekho 
# -------------------copy----------
li2=li
print(li)
print(li2)

li2.remove(-1000)
print(li)
print(li2)# agar hum copy nhi karenge to hum jo bhi changes karenge li2 mai vo li me bhi hoga 

li2=li.copy()
print(li)
print(li2)
li2.remove(True)
print(li)
print(li2)