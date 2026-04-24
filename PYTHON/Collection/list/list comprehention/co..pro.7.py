# give gread
l1=[23,54,76,36,98,56,73,62,81,47]
#with list comprehension
l2=[f"{i} A"if i>=90 else f"{i} B" if i>=70 else f"{i} C" if i>=50 else f"{i} D" if i>=33 else f"{i} fail" for i in l1]
print(l2)
for i in l2:
    print(i)