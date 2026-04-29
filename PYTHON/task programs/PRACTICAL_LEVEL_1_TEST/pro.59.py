#Q 59: Sum of Positive and Negative Numbers
# Write a function sum_positive_and_negative(lst) that accepts a list of integers and 
# returns a tuple with the sum of all positive numbers and the sum of all negative numbers.
def sum_positive_and_negative(lst):
    sum_p,sum_n=0,0
    for i in lst:
        if i<0:
            sum_n+=i
        else:
            sum_p+=i            
    return f'positive ={sum_p}', f'negative ={sum_n}'
print(sum_positive_and_negative([1,2,3,4,5,6,7,-1,5,-6,-4,-3,9,-2]))