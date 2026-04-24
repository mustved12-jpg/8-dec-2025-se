# save in list l2 only 4 charecter

l1=["java","mustved12","php","python","android","fluter"]
l2=[]
# witout list comprehension

for i in l1:
    if i.isalpha():
        l2.append(i[0:4])
print(l2)

# with list comprehension

l3=[i[:4] for i in l1 if i.isalpha()]

print(l3)

# jo bhi string ho uske 4 carector save kro 

l4=[name[:4] for name in l1 if type(name)==str]
print(l4)
