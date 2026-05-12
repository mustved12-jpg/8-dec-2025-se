"""Q  102: Find the Longest Key in a Dictionary
Write a function longest_key(d) that accepts a dictionary and 
returns the key with the longest length.

"""
d={'mustved':1,'python':2,'java':3,'android12':8}
def longest_key(d):
    name=None
    for i in d:
         name=i
         break
    for i in d:
        if len(name)<len(i):
            name=i
    return name
print(longest_key(d))