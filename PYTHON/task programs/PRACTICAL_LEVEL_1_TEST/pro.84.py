"""Q  84: Remove Duplicates from a List of Strings
Write a function remove_duplicates(lst) that accepts a list of 
strings and returns a new list with duplicate strings removed.

"""
def remove_duplicates(lst):
    l1=[]
    for i in lst:
        if i not in l1:
            l1.append(i)
    return l1

l1=['java','php','python','java','android','python','mustved','java','flutter']
print(remove_duplicates(l1))

#or
l1=list(set(l1))
print(l1)