"""Q  110: Count the Number of Even and Odd Numbers in a List
Write a function count_even_odd(lst) that accepts a list of integers and 
returns a dictionary with the count of even numbers and odd numbers.

"""
l1=[1,2,3,4,5,6,7,8,7,6,5,6,5,4,5,3,5,6,35,7,3,7,4,3,4,7,8,4,4,7,4,6,4]
def count_even_odd(lst):
    d={}
    c=0
    for i in lst:
        if i%2==0:
            c+=1
    d["even"]=c
    d['odd']=len(lst)-c
    return d
print(count_even_odd(l1))