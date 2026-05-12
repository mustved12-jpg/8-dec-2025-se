"""Q   107: Sum All Even Keys in a Dictionary
Write a function sum_even_keys(d) that accepts a 
dictionary with integers as keys and returns the sum of all keys that are even numbers.
"""
d={1:'ok',2:'ok',3:'ok',4:'ok',5:'ok',6:'ok',7:'ok',8:'ok',9:'ok',10:'ok'}
def sum_even_keys(d):
    Sum=0
    for i in d:
        if i%2==0:
            Sum+=i
    return Sum
print(sum_even_keys(d))