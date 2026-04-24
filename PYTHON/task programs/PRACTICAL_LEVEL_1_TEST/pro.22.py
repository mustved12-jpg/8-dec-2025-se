#Q 22: Write a function that accepts a string and a substring, and returns True if the substring is found in the string, otherwise False.
def myfun():
    main_name="im mustved and its smartphone"
    sub_name='ved'
    if sub_name in main_name:
        return True
    else:
        return False
print(myfun())