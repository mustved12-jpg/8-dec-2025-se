# Q 63: Fibonacci Sequence
# Write a function generate_fibonacci(n) that accepts a number n 
# and returns a list containing the first n numbers of the Fibonacci sequence.
def generate_fibonacci(n):
    l1=[]
    f,s=0,1
    for i in range(n):
        l1.append(f)
        f,s=f+s,f
    return l1
print(generate_fibonacci(5))