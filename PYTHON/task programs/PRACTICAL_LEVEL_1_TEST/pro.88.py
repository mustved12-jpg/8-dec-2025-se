"""Q  88: Count the Occurrence of Each Item in a List
Write a function count_items(lst) that accepts a list of items 
and returns a dictionary where the keys are the items from the list, and the 
values are the number of times each item appears.

"""
def count_items(lst):
    d={}
    for i in lst:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
l1=['pizza','vadapao','itly','dhosa','pizza','barger','pizza','itly']
print(count_items(l1))