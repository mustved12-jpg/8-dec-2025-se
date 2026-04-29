"""Q  90: Remove Duplicates from a List and Keep Order
Write a function remove_duplicates(lst) that accepts 
a list and removes any duplicate elements while keeping the original order of the elements.
"""
def remove_duplicates(lst):
    l1=[]
    for i in lst:
        if i not in l1:
            l1.append(i)
    return l1
l1=[1,2,3,1,5,2,6,3,1,7]
print(remove_duplicates(l1))