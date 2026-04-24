#Q 21: Write a function that accepts a string and returns the first non-repeating character in the string.
def myfun():
    name="i'am mustved and i'am good"
    re=''
    for i in name:
        if i==' ':
            continue
        no=0
        for j in name:
            if j==' ':
                continue
            if i==j:
                no+=1
        if no==1:
            re=i
            break
    return re
print("first non-repeating character =",myfun())