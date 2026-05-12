"""Q  108: Create a Frequency Dictionary from a List
Write a function create_frequency_dict(lst) that accepts a list and returns 
a dictionary where the keys are the elements of the list, and the values are the 
count of how often each element appears.
"""
l1=[1,2,'java',3,4,'mustved',3,4,5,'pyrhon','java']
def create_frequency_dict(lst):
    d={}
    for i in lst:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
print(create_frequency_dict(l1))