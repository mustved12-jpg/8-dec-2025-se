import re

# \d for digits
data=" my contect number is 9988776754 and my subject is pyhton"
result=re.search(r"\d+",data)
print(result)
print(result.group())