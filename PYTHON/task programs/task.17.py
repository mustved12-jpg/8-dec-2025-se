ol=[]
el=[]
for i in range(5):
    user=int(input("enter your number :"))
    if user%2==0:
        ol.extend(user)
    else:
        el.extend(user)

print(ol)
print(el)
