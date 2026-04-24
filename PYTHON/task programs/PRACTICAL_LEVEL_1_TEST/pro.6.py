#Q 6: Write a function that accepts a string and a character, and returns the number of times the character appears in the string.
def string():
    l1=[]
    name=input("enter your name :".upper())
    for i in name:
        if i not in l1:
            l1.extend([i,1])
        else:
            l1[l1.index(i)+1]+=1
    return print(l1)
string()
# in dictionary

def stri():
    d={}
    name=input("enter your name :".upper())
    for i in name:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return print(d)
stri()