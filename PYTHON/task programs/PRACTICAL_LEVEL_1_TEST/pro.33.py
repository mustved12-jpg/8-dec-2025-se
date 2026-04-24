#Q 33: Write a function that accepts a list of numbers and returns a new list with all the numbers that are divisible by both 2 and 3.
l1=[10,7,30,6]
l2=list(filter(lambda num: num%2==0 and num%3==0,l1))
print(f"{l1}\n{l2}")