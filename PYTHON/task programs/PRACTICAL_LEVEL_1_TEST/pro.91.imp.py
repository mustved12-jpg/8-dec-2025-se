"""Q  91: Sort a Dictionary by Value
Write a function sort_dict_by_value(d) that accepts a dictionary and returns
 a new dictionary sorted by its values in ascending order.
"""
def sort_dict_by_value(d):
    sot=dict(sorted(d.items(),key=lambda num: num[1]))
    return sot
d={'b':2,'d':4,'a':1,'c':3}
print(sort_dict_by_value(d))
print(d.items())#dict_items([('b', 2), ('d', 4), ('a', 1), ('c', 3)])
