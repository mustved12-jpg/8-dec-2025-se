# Write a Python program that uses a custom iterator to iterate over a list of integers.
l1=[1,2,3.10,4,-5,6,-7.54,8,-9,4.23,3,-5,-6,3,-5,0.7]
name=iter(filter(lambda num: type(num)==int,l1))
for i in range(int(max(l1))):
    print(next(name))