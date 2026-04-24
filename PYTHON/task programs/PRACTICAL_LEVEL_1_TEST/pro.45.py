#Q 45: Write a function that accepts a string and returns the longest word in the string.
name="hello my namgdge is mustved"
name=name.split()
first_len=name[0]
for i in name:
    if len(i)>len(first_len):
        first_len=i 
print(first_len)