#Q 47: Write a function that accepts a list of numbers and returns the smallest number that is divisible by both 4 and 5.
l1=[45,50,40,20,30,60,80]
l1.sort()
num=0
for i in l1:
    if i%4==0 and i%5==0:
        num=i
        break 
print(num)

#_____________________________
l2=[i for i in l1 if i%4==0 and i%5==0]
print(min(l2))