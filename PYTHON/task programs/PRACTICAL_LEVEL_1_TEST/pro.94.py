"""Q  94: List of Keys with Minimum Value
Write a function min_value_keys(d) that accepts a dictionary 
and returns a list of keys that have the minimum value in the dictionary.
"""
def min_value_keys(d):
    l1=[]
    m=min(d.values())
    for k,v in d.items():
        if v==m:
            l1.append({k:v})# agar humko ek hi dena hai to d={k:v} and d return kra do 
    return l1
d={'a':10,'b':50,'c':23,'d':30,'e':50}
print(min_value_keys(d))