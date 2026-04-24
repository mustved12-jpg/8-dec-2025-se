#save only even number in list

l1=[]
#without list comprehension
for i in range(1,11):
    if i%2==0:
        l1.append(i)

print(l1)

#with list comprehension

l2=[i for i in range(1,11) if i%2==0]# it's called right condition
#{agar humco only i condition lgana ho to hum if ko right side likhte hai varna pro2 dekho}
print(l2)

l3=[i for i in range(1,11) if i>=5]
print(l3)