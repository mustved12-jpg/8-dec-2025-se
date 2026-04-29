# Q 60: Check if a String is a Substring
# Write a function is_substring(str1, str2) that accepts two strings and checks if the first 
# string is a substring of the second string. Return True or False.
def is_substring(str1, str2):
    if str1 in str2:
        return True
    else:
        return False
name1='yth'
name2='im mustved and im python developer'
print(is_substring(str1=name1,str2=name2))
