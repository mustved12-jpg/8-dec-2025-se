#Q 32: Write a function that accepts a list of strings and returns a new list where each string is capitalized.
l1=['java','python','php','android','flutter','java']
l2=[i.capitalize() for i in l1]
print(f"{l1}\n{l2}")