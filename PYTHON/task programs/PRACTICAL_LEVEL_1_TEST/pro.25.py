#Q 25: Write a function that accepts a list of numbers and returns the number of negative numbers in the list.
l1=[3,4,5,6,7,8,9,-6,4,3,5,-9,2,5,-3,-65]
l2=list(filter(lambda num: num<0,l1))
print(l2)
l3=[i for i in l1 if i<0]
print(l3)