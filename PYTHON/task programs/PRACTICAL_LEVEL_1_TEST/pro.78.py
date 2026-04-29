"""Q  78: Calculate Simple Interest
Write a function calculate_simple_interest(principal, rate, time) 
that accepts the principal, rate of interest, and time, and returns the calculated simple interest.

"""
def calculate_simple_interest(principal, rate, time):
    to=(principal*rate)/100
    to=to*time
    return to
print(calculate_simple_interest(1000,8,2))