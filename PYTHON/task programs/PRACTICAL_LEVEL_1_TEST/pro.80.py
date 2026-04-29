"""Q  80: Generate Multiplication Table
Write a function generate_multiplication_table(n) 
that accepts a number n and prints its multiplication table (from 1 to 10).

"""
def generate_multiplication_table(n):
    l=[]
    for i in range(1,11):
        l.append(f'{n} x {i} = {n*i}')
    return l
for i in generate_multiplication_table(5):
    print(i)