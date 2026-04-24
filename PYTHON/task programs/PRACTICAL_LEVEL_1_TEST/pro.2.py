#Q 2: Write a function that accepts a string and returns True if the string is a palindrome, and False otherwise.
def string():
    name=input("enter your name :".upper())
    if name==name[::-1]:
        return True
    else:
        return False

print(string())
