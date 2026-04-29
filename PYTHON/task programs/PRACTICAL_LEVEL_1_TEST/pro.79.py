"""Q  79: Find Unique Elements in List
Write a function find_unique_elements(lst) 
that accepts a list and returns a new list containing only the unique elements from the original list.
"""
def find_unique_elements(lst):
    lst=list(set(lst))
    return lst
print(find_unique_elements([1,2,3,4,5,4,3,7,3,7,2,4,8,42,5,6,7,1]))