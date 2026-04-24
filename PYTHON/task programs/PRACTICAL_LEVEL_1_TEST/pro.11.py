#Q 11: Write a function that accepts a list of numbers and returns a new list with the squares of all the numbers in the list.
def squer():
    l1=[2,3,4,5,6,7]
    l2=[]
    for i in l1:
        l2.append(i*i)
    return l2
print(squer())