"""Q   103: Check if a List Contains Only Unique Elements
Write a function is_unique(lst) that accepts a list and returns True if all the elements are unique, 
and False if any element appears more than once.

"""
l1=[1,'mustved',8,3,'java','python']
def is_unique(lst):
    for i in lst:
        if lst.count(i)==1:
            f=1
        else:
            return False
    if f==1:
        return True

print(is_unique(l1))