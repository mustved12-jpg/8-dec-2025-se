# Q 55: Remove Whitespace from a String :Write a function remove_whitespace(s) that accepts a 
# string and returns the string with all leading, trailing, and extra spaces between words removed.
def remove_whitespace(s):
    s.strip()
    name=''
    for i in s:
        if i==" ":
            continue
        else:
            name+=i
    return name
print(remove_whitespace('    im mustved ok    '))