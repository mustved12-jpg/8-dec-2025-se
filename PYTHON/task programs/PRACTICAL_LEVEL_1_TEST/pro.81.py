"""Q  81: Create a Dictionary from Two Lists
Write a function create_dict(keys, values) that accepts two lists, keys and values,
and returns a dictionary where the keys are from the first list and the values are from the second list.

"""
def create_dict(keys, values):
    d=dict(zip(keys,values))
    return d
print(create_dict(['a','b','c'],[1,2,3]))