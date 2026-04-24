#Q 8: Write a function that accepts a list of numbers and returns the average of the numbers.
def ave():
    l1=[]
    for i in range(1,6):
        number=int(input(f"enter your {i} number :".upper()))
        l1.append(number)
    return sum(l1)/len(l1)

print(ave())