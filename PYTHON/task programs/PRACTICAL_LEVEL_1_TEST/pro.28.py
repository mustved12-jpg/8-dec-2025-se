#Q 28: Write a function that accepts a string and removes all duplicate characters from the string.
l1=['java','python','php','android','flutter']
l2=[]
for i in l1:
    name=''
    for j in i:
        if j not in name:
            name=name+j
    l2.append(name)
print(l2)