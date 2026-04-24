l1=["java",'python','php','android','flutter']
def myfun(name):
    return name.upper()

l2=list(map(myfun,l1))
print(f"{l1}\n{l2}")

#with lambda
l3=list(map(lambda n: n.title(),l1))
print(l3)
#               OR
l4=list(map(str.title,l1))#bina lambada ke uva q ki title bhi ak function hai but string ho to str ke alava 
print(l4)#                  dusra name nhi e sakte 