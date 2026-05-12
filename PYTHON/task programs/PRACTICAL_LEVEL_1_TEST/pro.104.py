"""Q  104: Convert a Dictionary to a List of Tuples
Write a function dict_to_tuples(d) that accepts a dictionary and returns
 a list of tuples where each tuple contains a key-value pair from the dictionary.

"""
d={1:10,2:20,3:30}
def dict_to_tuples(d):
    t=list(d.items())
    return t
print(dict_to_tuples(d))