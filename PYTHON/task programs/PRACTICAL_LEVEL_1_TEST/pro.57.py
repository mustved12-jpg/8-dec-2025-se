#Q 57: Find Missing Number in Sequence
#Write a function find_missing_number(numbers) that accepts a list of numbers from 1 to N, 
# with one number missing. The function should return the missing number.
def find_missing_number(numbers):
    miss_num=[i for i in range(1,max(numbers)+1) if i not in numbers]
    return miss_num
l1=[12,2,7,6,15,9,2,6,8,11,18,16]
print(find_missing_number(l1))