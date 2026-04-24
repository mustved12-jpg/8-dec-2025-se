#Q 52: Sum of Digits in a String
# Write a function sum_of_digits_in_string(s) that accepts a string containing 
# alphanumeric characters and returns the sum of all digits found in the string.
def sum_of_digits_in_string(n):
    total=0
    for i in n:
        if i.isnumeric():
            total+=int(i)
    return total
        
print(sum_of_digits_in_string('8must12ved46'))