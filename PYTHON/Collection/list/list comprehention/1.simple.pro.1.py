l1=[]

# without list comprehension

for i in range(1,6):
    l1.append(i)

print(l1)

# with list compehension

l2=[i for i in range(1,6)]
print(l2)