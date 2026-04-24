#Q 12: Write a function that accepts a string and counts how many vowels are in the string.
def count():
    v_count=0
    name=input("enter your name :")
    for i in name:
        match i:
            case 'a'|'e'|'i'|'o'|'u':
                v_count+=1
    return v_count
print(count())