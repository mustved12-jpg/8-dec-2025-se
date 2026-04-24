# find palidrom
l1=["mom","world","level","number","madam","java","python"]
l2=[]
#without list comprehension
for i in l1:
    if i==i[::-1]:
        l2.append(f"{i} is palindrom")
    else:
        l2.append(f"{i} not palindrom")

print(l2)

# with list comprehension

l3=[f"{i} is palindrom" if i==i[::-1] else f"{i} not palindrom" for i in l1]
print(l3)