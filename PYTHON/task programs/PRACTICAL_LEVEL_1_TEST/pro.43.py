#Q 43: Write a function that accepts a list of numbers and returns the average of the numbers, excluding any zero values.
l1=[10,20,3,6,0,5]
l2=[i for i in l1 if i!=0]
print(sum(l2)/len(l2))