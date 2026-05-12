"""Q  96: Check if a Dictionary Contains a Specific Key
Write a function contains_key(d, key) that accepts a dictionary and a key. 
It should return True if the key exists in the dictionary and False otherwise.

"""
def contains_key(d, key):
    if key in d.values():
        return True
    else:
        return False
d={'name1':"aaa",'name2':"bbb",'name':'ccc'}
k='cc5'
print(contains_key(d,k))