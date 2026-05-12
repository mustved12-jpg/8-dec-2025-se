"""Q  99: Group List Elements by Frequency
Write a function group_by_frequency(lst) that accepts a list and groups
 the elements based on their frequency. The function should return a dictionary 
 where the keys are the frequencies and the values are lists of elements that occur that many times.

"""
l1=[1,2,3,4,10,7,3,1,5,9,6,1,7,8,2,9,6,5,6,2,4,1,8,15,4]
def group_by_frequency(lst):
    d={}
    for i in lst:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
print(group_by_frequency(l1))