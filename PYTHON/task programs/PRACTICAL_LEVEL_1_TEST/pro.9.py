#Q 9:Accept a string from the user and print it in uppercase if the length of the string is greater than 5, else print it in lowercase using a function.
def up():
    name=input("enter your name :".upper())
    if len(name)>5:
        return name
    else:
        return name.upper()
print(up())