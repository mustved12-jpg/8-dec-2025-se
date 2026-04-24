#Q 46: Write a function that accepts a list of integers and returns the median value of the list.
l1=[1,2,3,4,8,6,7,8,9]
l1.sort()
print(l1)
if len(l1)%2==0:
    print("madian number =",(l1[(len(l1)//2)-1]+l1[len(l1)//2])/2)
else:
    print("madian number =",l1[len(l1)//2])

"""         ruls
Input List               Sorted                  Median
[3, 1, 5, 7, 2]         [1,2,3,5,7]                3
[3, 1, 5, 7]            [1,3,5,7]                 4.0 
[10]                    [10]                      10

"""