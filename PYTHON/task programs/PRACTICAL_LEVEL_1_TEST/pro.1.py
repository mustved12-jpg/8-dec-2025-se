#Q 1: Accept a number from the user and find the factorial of the number using a function with a parameter and return type.
def fec(a):
    f=1
    for i in range(1,a+1):
        f*=i
    return f
num=int(input("enter your number :".upper()))
print(f"{num} factoriyal number =",fec(num))
