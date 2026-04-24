#Q 49: Write a function that accepts a string and returns the string with each word reversed, but the order of the words remains the same.
name='im mustved and im the boss'.split()
name1=""
for i in name:
    name1+=' '+i[::-1]
name1=name1.lstrip()
print(name1)
name3=" ".join(name)
print(name3)