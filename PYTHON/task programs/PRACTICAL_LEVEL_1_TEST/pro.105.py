"""Q  105: Find Missing Numbers in a List
Write a function find_missing_numbers(lst, n) that accepts a list of integers
and a number n. The list contains integers from 1 to n with some numbers missing.
The function should return a list of the missing numbers.
"""
l1=[1,2,4,6,-4,15,3,8,4,10,13,15]
def find_missing_numbers(lst, n):
    l1=[]
    for i in range(min(lst),n+1):
        if i not in lst:
            l1.append(i)
    return l1
print(find_missing_numbers(l1,20))
