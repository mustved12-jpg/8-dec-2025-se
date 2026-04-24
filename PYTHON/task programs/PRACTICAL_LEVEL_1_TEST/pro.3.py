#Q 3: Write a function that accepts a list of numbers and returns the sum of all even numbers in the list.
def li():
    l1=[]
    sume=0
    for i in range(1,6):
        num=int(input(f"enter your {i} number :"))
        l1.append(num)
        if num%2==0:
            sume+=num
    print(l1)
    return sume
print(li())

#static
def li2():
    l1=[4,5,6,7,8,2,4]
    sume=0
    for i in l1:
        if i%2==0:
            sume+=i
    return sume
print(li2())