# user se input leke number or string ko alag karo

l5=[]# ye ek hi list me ho jaye ga 
for i in range(5):
    user=input(f"enter your name {i+1} : ")
    if user.isalpha():
       l5.append(user) 
    else:
        user=int(user)
        l5.append(user)
print(l5)

# with list comprehension
l1=[]# isme pehle sub values save hogi fi l2 mai comprehension kar ke sav krenge isme do list bne gi
for i in range(1,6):
    name=input("enter your name :")
    l1.append(name)
l2=[int(i) if i.isnumeric() else i for i in l1]
print(l1)
print(l2)