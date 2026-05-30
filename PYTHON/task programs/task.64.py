data=input("enter a number :")#31*23-21+3-213%12-312+123%12
loop=data
numbers=[]
opereter=""
num=""
for i in loop:
    if i in "*+-%/":
        opereter+=i
        numbers.append(num)
        num=""
    else:
        num+=i
numbers.append(num)
print(f"{numbers}\n{opereter}")