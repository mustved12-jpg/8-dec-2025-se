"""Q  93: Find the Key with the Maximum Value in a Dictionary
Write a function find_max_key(d) that accepts a dictionary and returns the key that has the
highest value. If there are multiple keys with the same maximum value, return any one of them.
"""
def find_max_key(d):
    l1=[]
    m=max(d.values())
    for k,v in d.items():
        if v==m:
            l1.append({k:v})# agar humko ek hi dena hai to d={k:v} and d return kra do 
    return l1
d={'a':10,'b':50,'c':23,'d':30,'e':50}
print(find_max_key(d))