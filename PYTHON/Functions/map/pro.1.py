#without map
l1=[12,2,32,45,14,56,78,38,92,7,82,54,85,64,2,75,25,3,87]
l2=[]
for i in l1:
    l2.append(i+5)
print(f"{l1}\n{l2}")

#with map function
l3=list(map(lambda num: num+5,l1))
print(l3)

#----------------------------------------------

#with and without lambad map
l1=[12,2,32,45,14,56,78,38,92,7,82,54,85,64,2,75,25,3,87]
def myfun(a):
    if a%2==0:
        return f"{a} even"
    else:
        return f"{a} odd"
l2=list(map(myfun,l1))
print(l2)

#with lambad
l1=[12,2,32,45,14,56,78,38,92,7,82,54,85,64,2,75,25,3,87]
l2=list(map(lambda num:f"{num} even" if num%2==0 else f"{num} odd",l1))
print(l2)