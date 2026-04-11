li=["java","python","php","android","flutter"]
l2=li[::]
#l2.remove("java")
print(li)
print(l2[0][::-1])

for i in range(0,len(l2),+1):
    l2.insert(i,l2[i][::-1])
    l2.pop(i+1)

print(l2)