# Q 53: Remove Duplicate Words
# Write a function remove_duplicate_words(sentence) that accepts a string with multiple words and 
# returns a new string where all duplicate words are removed while maintaining the original order of words.
def remove_duplicate_words(sentence):
    name=''
    for i in sentence:
        if i not in name:
            name+=" "+i
    return name.lstrip()
name='java python php java android flutter php mustved java'.split()
print(remove_duplicate_words(name))