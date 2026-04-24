#Q 5: Accept a number from the user and check if it is a prime number using a function with a parameter and return type.
def pri(a):
    for i in range(2,a):
        if a%i==0:
            return "not a palindrom"
    return "palindrom"
number=int(input("enter your number :".upper()))
print(pri(number))