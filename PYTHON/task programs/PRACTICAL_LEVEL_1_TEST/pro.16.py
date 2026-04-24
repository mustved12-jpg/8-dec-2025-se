#Q 16: Write a function that accepts a number and returns the sum of its digits.
def num():
    number=int(input("enter your number :"))
    sume=0
    while number:
        sume+=number%10
        number=int(number/10)
    return print(sume)
num()

def stringnum():
    number=int(input("enter your number :"))
    number=str(number)
    total=0
    for i in number:
        total+=int(i)
    return print(total)
stringnum()

# _______________________using of lambda and list
naem=input("enter your name :")
naem=str(naem)
to=list(map(lambda num: int(num),naem))
print(sum(to))