"""                                         :::generator:::
generator is a spacial function which is generate some state of value and store in a one place and return
as per the requirement

normal function perform any operation and return value but generator dose not return it just store value 
and save state and return using (yield) keyword
"""

def myfun():
    return 1
    return 2
    return 3
# jab bhi hum isko call karen ge ye 1 hi retun kare ga 
print(myfun())#1
print(myfun())#1

def mygenerator():
    yield 1
    yield 2
    yield 3
obj=mygenerator()
print(next(obj))#1
print(next(obj))#2
print(next(obj))#3
print(next(mygenerator()))# agar me ye likhun ga to ye har bar functoi 1 se stat karega 
print(next(obj))# 4 nhi hai to erorr aye gi
