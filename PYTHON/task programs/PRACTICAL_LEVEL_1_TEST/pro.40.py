#Q 40: Write a function that accepts a number and prints whether it is a perfect number 
# (a number that is equal to the sum of its divisors, excluding the number itself).
number=6
total=0
for i in range(1,number):
    if number%i==0:
        total+=i
if number==total:
    print(f'{number} is perfect.')
else:
    print(f'{number} is not perfect.')