# esi string ko save kro jiski lenth 4 se jyada ho
l1=["java","python","php","android","c++","fluter"]
l2=[]
#without list comprehension

for i in l1:
    if len(i)>4:
        l2.append(i)
print("l2 =",l2)

# with list comprehension

l3=[i for i in l1 if len(i)>4]
print("l3 =",l3)