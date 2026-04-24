#Q 29: Write a function that accepts a list of integers and returns the sum of all numbers greater than 10.
l1=[23,423,12,10,9,4,23]
l2=[i for i in l1 if i>10]
print(l2)
print(sum(l2))
#____________________________
total=0
for i in l1:
    if i>10:
        total+=i
print(total)