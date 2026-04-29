# Q 62: Generate a List of Prime Numbers
# Write a function generate_primes(n) that accepts a number n and returns a list of all prime numbers less than or equal to n.
def generate_primes(n):
    l1=[]
    for i in range(2,n+1):
        f=0
        for j in range(2,i):
            if i%j==0:
                f=1
                break
            else:
                f=0
        if f==0:
            l1.append(i)
    return l1

print(generate_primes(23))