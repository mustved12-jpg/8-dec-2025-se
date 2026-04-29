"""Q  92: Sum All Values in a Dictionary
Write a function sum_dict_values(d) that accepts a dictionary 
where the values are numbers. The function should return the sum of all values in the dictionary.
"""
def sum_dict_values(d) :
    d=sum(d.values())
    return d
d={'b':2,'d':4,'a':1,'c':3}
print(sum_dict_values(d))