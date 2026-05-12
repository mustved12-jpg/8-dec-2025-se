"""Q  98: Find the Difference Between Two Lists
Write a function find_difference(lst1, lst2) that accepts two lists and returns
 a new list containing elements that are in the first list but not in the second.

"""
l1=[1,2,3,4,5]
l2=[3,6,7,8,3,4,5,1,]
def find_difference(lst1, lst2):
    l1=[i for i in lst2 if i not in lst1]
    return l1
print(find_difference(l1,l2))