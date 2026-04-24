#Q 26: Write a function that accepts a string and returns the number of words in the string.
name="im mustved"
l1=[]
for i in name:
    if i==" ":
        continue
    if i not in l1:
        l1.extend([i,1])
    else:
        l1[l1.index(i)+1]+=1
print(l1)