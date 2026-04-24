# Q 19: Write a function that accepts a list of numbers and returns the product of all the numbers in the list.
l1=[1,2,3,4,5,6,-4]
def myfun(lis):
    total=1
    for i in range(len(lis)):
        total*=lis[i]
    return total
print("product =",myfun(l1))
