import re
#\d for only numbers

data="ram is 26 years old jay is 15 years old ramesh is 45 years old"
result=re.findall(r"\d+",data)
print(result)

# \D for not numbers
data="hello all my name is mustved im 887 ok but nyy number is 7556"
result=re.findall(r"\D",data)
print(result)
print("".join(result))
# \w for no symbols
data="my name is = mustved and my email is = ghghv@gmail.com"# @,=,space 
result=re.findall(r"\w",data)
print("".join(result))
# \W only symbols
data="mustved@gmail.com"
result=re.findall(r"\W",data)
print("".join(result))#@.

