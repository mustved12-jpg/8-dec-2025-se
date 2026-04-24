#Q 10: Write a function that accepts a list of numbers and returns a new list with only the numbers that are divisible by 3.
def nume():
    l1,l2=[],[]
    for i in range(5):
        number=int(input(f"enter your {i+1} number :".title()))
        l1.append(number)
        if number%3==0:
            l2.append(number)
    print(l1,l2)
    return l2
print(nume())
        