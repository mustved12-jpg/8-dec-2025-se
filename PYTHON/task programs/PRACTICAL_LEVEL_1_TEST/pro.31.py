#Q 31: Write a function that accepts a string and returns the number of times a given word appears in the string.
name1="hello good mornig im good".split()
name2='good'
c=0
for i in name1:
    print(i)
    if i==name2:
        c+=1
print(f"<{name2}> appears in {c} times.".title())