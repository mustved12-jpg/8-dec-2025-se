# Write a generator function that generates the first 10 even numbers.
def my(num):
    for i in num:
        if i%2==0:
            yield i
l1=[1,25,13,24,75,36,7,2,33,44,55,66,78,12,23,54,23,8,74,29]
ev=my(l1)
for i in range(10):
    print(next(ev))