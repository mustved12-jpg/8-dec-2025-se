#Q 50: Write a function that accepts a list of strings and returns a new list containing only the strings that start with a vowel.
l1=['java','python','android','oython','fullter','iullter']
l2=[]
for i in l1:
    match i[0]:
        case 'a'|'o'|'e'|'i'|'u':
            l2.append(i)
print(l2)

#or
l3=[]
for i in l1:
    if i.startswith(('a','e','i','o','u')):
        l3.append(i)
print(l3)