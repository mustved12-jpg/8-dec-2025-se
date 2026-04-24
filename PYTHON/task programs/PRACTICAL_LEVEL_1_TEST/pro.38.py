#Q 38: Write a function that accepts a list of integers and returns a new list with all the positive numbers squared.
l1=[-3,-2,-1,0,1,2,3,4]
l2=[i*i for i in l1 if i>0]
print(f'{l1}\n{l2}')