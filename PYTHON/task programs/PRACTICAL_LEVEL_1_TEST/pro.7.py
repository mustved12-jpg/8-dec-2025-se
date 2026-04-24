#Q 7: Write a function that accepts a list of strings and returns a new list with each string reversed.
def reve(l1):
    l2=[]
    for i in l1:
        l2.append(i[::-1])
    return print(l2)
l1=['java','python','php','android','c++']
reve(l1)

# saving one one charecter
def reve(l1):
    l2=[]
    for i in l1:
        name=""
        for j in range(len(i)-1,-1,-1):
            name+=i[j]
        l2.append(name)
    return print(l2)
l1=['java','python','php','android','c++']
reve(l1)