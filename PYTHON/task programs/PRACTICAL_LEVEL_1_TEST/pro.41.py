#Q 41: Write a function that accepts a string and returns the string with all vowels removed.
name='hello my Name is mustved'.lower()
name2=""
for i in name:
    match i:
        case 'a'|'o'|'i'|'e'|'u':
            pass
        case _:
            name2+=i
print(name2)