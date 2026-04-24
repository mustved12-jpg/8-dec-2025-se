#Q 24: Write a function that accepts a list of numbers and returns the number of prime numbers in the list.
l1=[12,32,35,65,84,7,13,4,76,58,45,17,91,3,9,29,68]
l2=[]
for i in l1:
    f=0
    for j in range(2,i):
        if i%j==0:
            f=1
            break
    if f==0:
        l2.append(i)        
print(l2)