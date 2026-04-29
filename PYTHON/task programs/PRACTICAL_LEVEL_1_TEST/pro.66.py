"""Q  66: Concatenate Strings with a Separator
Write a function concatenate_with_separator(lst, separator) that accepts a list of strings and a separator 
string, then returns a new string where all elements of the list are joined using the separator.

"""
def concatenate_with_separator(lst, separator):
    name=separator.join(lst)
    return name
l1=['aer','dasb','wefc']
print(concatenate_with_separator(lst=l1,separator="-"))