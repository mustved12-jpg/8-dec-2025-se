"""Q  87: Merge Two Dictionaries
Write a function merge_dicts(dict1, dict2) that accepts 
two dictionaries and merges them into one. If there are overlapping keys, 
the values from the second dictionary should overwrite the values from the first.

"""
def merge_dicts(dict1, dict2):
    d=dict1
    for k,v in dict2.items():
        d[k]=v
    return d
d1={'a':1,'b':2,'c':3}
d2={'A':11,'B':12,'C':13,'a':21}
print(merge_dicts(d1,d2))
