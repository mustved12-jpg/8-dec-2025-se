"""Q  76: Convert a String to Title Case
Write a function to_title_case(sentence) that accepts a string and 
returns the string in title case (the first letter of each word capitalized).

"""
def to_title_case(sentence):
    sentence=sentence.title()
    return sentence
print(to_title_case("im mustved im python developer"))