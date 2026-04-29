"""Q  77: Count the Occurrence of Each Character
Write a function count_character_occurrences(string) that 
accepts a string and returns a dictionary with the count of each character in the string.

"""
def count_character_occurrences(string):
    d={}
    for i in string:
        if i==" ":
            continue
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
print(count_character_occurrences('im mustved im pytohn developer'))

