a=[1,2,3]
b=[1,2,3]

print(id(a))
print(id(b))

print(a==b)# true
print(a is b)# False

print(a[0] is b[0])# True
