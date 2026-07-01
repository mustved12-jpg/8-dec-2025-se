arr = [1,2,3,[4,5]]
a=[]
def my(ok):
    print(type(ok))
    for i in ok:
        if type(i)==list:
            my(i)
        else:
            a.append(i)    
for i in arr:
    if type(i)==list:
        my(i)
    else:
        a.append(i)
print(a)