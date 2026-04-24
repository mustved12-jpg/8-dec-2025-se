num1=int(input("enter your number 1 : "))
num2=int(input("enter your number 2 : "))

if num1>num2:
    print(f"{num1} is greter number. \n{num2} is less number.")
else:
    print(f"{num2} is greter number. \n{num1} is less number.")

for i in range(2,num1):
    if num1%i==0:
        print("not prime number.")
        break
    else:
        if i==num1-1:
            print("prime number.")

if num1>=80:
    print("A gread.")
elif num1>=60:
    print("B gread.")
elif num1>=45:
    print("C gread.")
elif num1>=33:
    print("D gread.")
else:
    print("fail")


if num1>=1 and num1<=100:
    if num1>=18:
        print("eligible.")
    else:
        print("not eligible.")
    
list1=["apple","banana","mango"]

for ver in list1:
    print(ver)

for ver in list1:
    print(len(ver))

for ver in list1:
    if ver=="apple":
        print(ver)


