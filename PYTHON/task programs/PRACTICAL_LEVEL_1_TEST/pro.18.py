#Q 18: Write a function that accepts a list of integers and returns the second largest number in the list.
def integers():
    l1=[19,82,36,54,75,61,47,'name',54.98,True]
    l2=[i for i in l1 if type(i)==int]
    print(f'{l1}\n{l2}')
    l2.sort()
    return l2[-1],l2[-2]
num1,num2=integers()
print('largest number =',num1)
print('second largest number =',num2)