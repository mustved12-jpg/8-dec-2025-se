#Q 37: Write a function that accepts a string and returns a dictionary where the keys are the characters 
# and the values are the counts of those characters in the string.
def myfun():
    d={}
    name='im mustved'
    for i in name:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1
    return d
print(myfun())