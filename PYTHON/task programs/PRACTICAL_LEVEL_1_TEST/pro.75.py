"""Q  75: Find the Longest Word in a Sentence
Write a function longest_word(sentence) that accepts 
a sentence and returns the longest word in the sentence.

"""
def longest_word(sentence):
    sentence=list(sentence.split())
    sentence.sort(key=lambda num: len(num))
    l1=[i for i in sentence if len(i)==len(sentence[-1])]
    return l1
print(longest_word("hello im mustved and im python developer hmm yes oohh ok"))
