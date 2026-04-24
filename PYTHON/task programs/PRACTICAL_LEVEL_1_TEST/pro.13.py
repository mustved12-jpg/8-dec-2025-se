#Q 13: Write a function that accepts a number and prints its multiplication table from 1 to 10.
def num():
    number=int(input("enter your number :"))
    for i in range(1,11):
        mul=i*number
        print(f"{number}x{i}={mul}")
num()