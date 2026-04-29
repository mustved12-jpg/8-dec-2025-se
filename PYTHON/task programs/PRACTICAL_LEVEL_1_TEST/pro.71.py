"""Q  71: Merge Two Dictionaries
Write a function merge_dicts(dict1, dict2) that accepts two dictionaries and 
returns a single dictionary that contains the merged key-value pairs from both dictionaries.

"""
def merge_dicts(dict1, dict2):
    di1=dict(zip(dict1,dict2))
    di2=dict(zip(dict1.values(),dict2.values()))
    print(di1)
    print(di2)
    td=dict1
    for k,v in dict2.items():
        td[k]=v
    return td
d1={'a':1,'b':2,'c':3}
d2={'A':11,'B':12,'C':13}
print(merge_dicts(d1,d2))