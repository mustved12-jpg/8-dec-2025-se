#Q 4: Write a function that accepts a list of numbers and returns the maximum value in the list.
def li():
    l1=[]
    for i in range(1,6):
        num=int(input(f"enter your {i} number :".upper()))
        l1.append(num)
    return max(l1)

print(li())
