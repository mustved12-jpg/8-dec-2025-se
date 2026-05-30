import re
data="python is most populer programing language"
print(data)
result=re.search("populer",data)
print(result)
result=re.match("populer",data)
print(result)

"""
diffrent between match and search:
search : 
~> check each eliment of string

match:
~> check first eliment of the string if it dose not match it will return none
"""