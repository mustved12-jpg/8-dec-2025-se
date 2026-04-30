"""Q  95: Combine Multiple Lists into a Dictionary
Write a function combine_lists_to_dict(keys, values) that accepts two 
lists, one containing keys and the other containing values. The function should combine
them into a dictionary and return it. If there are more values than keys, ignore the extra values.
"""
l1=[1,2,3,6]
l2=['a','b','c']
def combine_lists_to_dict(keys, values):
    d=dict(zip(l2,l1))
    return d
print(combine_lists_to_dict(keys=l2,values=l1))