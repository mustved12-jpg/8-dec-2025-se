#Q 48: Write a function that accepts a number and returns a list of all the divisors of the number.
l1=[]
num=int(input("enter your number :"))
for i in range(1,num+1):
    if num%i==0:
        l1.append(i)
print(l1)



"""
12 ke divisors →

12 / 1  = 12 ✅
12 / 2  = 6  ✅
12 / 3  = 4  ✅
12 / 4  = 3  ✅
12 / 5  = 2.4❌ (perfectly nahi gaya)
12 / 6  = 2  ✅
12 / 12 = 1  ✅

Answer = [1, 2, 3, 4, 6, 12] ✅"""