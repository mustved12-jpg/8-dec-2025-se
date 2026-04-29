"""Q  74: Print Prime Numbers in a Range
Write a function print_primes_in_range(start, end) that accepts two numbers and prints all 
prime numbers between start and end (inclusive).

"""
def print_primes_in_range(start, end):
    l1=[]
    for i in range(start,end+1):
        for j in range(2,i):
            if i%j==0:
                f=1
                break
            else:
                f=0
        if f==0:
            l1.append(i)
    return l1
print(print_primes_in_range(10,30))