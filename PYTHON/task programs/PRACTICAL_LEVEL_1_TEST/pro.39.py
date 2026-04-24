#Q 39: Write a function that accepts a list of strings and returns a list of the strings with their lengths.
l1=['java','python','php','android','flutter']
l2=[f"{i} = {len(i)}"for i in l1]
print(l2)