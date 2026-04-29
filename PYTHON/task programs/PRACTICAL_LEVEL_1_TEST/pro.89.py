"""Q  89: Create a Dictionary from Two Lists
Write a function create_dict(keys, values) that accepts two lists: 
one containing keys and the other containing values. The function should return a 
dictionary with the keys from the first list and the corresponding values from the second list.
"""
def create_dict(keys, values):
    d=dict(zip(keys,values))
    return d
l1=['a','b','c']
l2=[1,2,3]
print(create_dict(l1,l2))