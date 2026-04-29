"""Q  86: Find the Most Frequent Element in a List
Write a function find_most_frequent(lst) that accepts a list of 
elements and returns the most frequent element in the list. If there are multiple frequent 
elements, return any one of them.
"""

l1=[1,'java',2,3,1,'ok',4,3,1,2,'nice','java','java',3]
def find_most_frequent(lst):
    d={}
    for i in l1:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    ok=d[1]
    l2=[k for k,v in d.items() if ok<=v]
    return l2
print(find_most_frequent(l1))

#or---------------
from collections import Counter

d=dict(Counter(l1))
for i in d:
    m=i# m me first vale ki key save hui
    break
l2=[k for k,v in d.items() if d[m]==v]
print(l2)