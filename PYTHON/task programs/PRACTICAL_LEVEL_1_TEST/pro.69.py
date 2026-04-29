"""Q  69: Find the First Repeating Element
Write a function find_first_repeating_element(lst) that accepts a list of integers
and returns the first element that repeats. If no element repeats, return None.

"""
def find_first_repeating_element(lst):
    n=None
    for i in lst:
        if lst.count(i)>1:
            n=i
            break
    return n
        
print(find_first_repeating_element([1,2,3,-4,4,5,6,-1,-4,5,-3,3]))