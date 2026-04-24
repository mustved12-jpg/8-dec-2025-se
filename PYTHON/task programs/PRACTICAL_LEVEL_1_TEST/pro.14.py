#Q 14: Write a function that accepts a list of strings and returns the longest string in the list.
def Long():
    l1=['java','pyhotn','php','c++','android']
    lon=l1[0]
    for i in l1:
        if len(lon)<len(i):
            lon=i 
    return lon
print(Long())