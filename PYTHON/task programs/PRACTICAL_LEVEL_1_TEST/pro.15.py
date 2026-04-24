#Q 15: Write a function that accepts a number and checks if it is an Armstrong number.
def num():
    number=int(input("enter your number :".title()))
    number=str(number)
    total=0
    for i in number:
        a=int(i)**len(number)
        total+=a
    print(number)
    if total==int(number):
        return print("armstrong number".upper())
    else:
        return print("not a armstrong number!!!".upper())
num()