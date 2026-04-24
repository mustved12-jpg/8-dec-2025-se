#Q 35: Write a function that accepts a list of integers and returns the count of even numbers in the list.
l1=[1.2,2,3,4,5,6,7,8,9]
l2=[i for i in l1 if type(i)==int and i%2==0]
print(f'{l1}\n{l2}')
print(len(l2))