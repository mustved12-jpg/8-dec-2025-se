"""Q  111: Check if a Dictionary is Empty
Write a function is_empty(d) that accepts a dictionary and returns 
True if the dictionary is empty, otherwise False.

"""
def is_empty(d):
    if d=={}:
        return True
    else:
        return False
d={}
print(is_empty(d))