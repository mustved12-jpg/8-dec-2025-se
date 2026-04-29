"""Q  83: Count Occurrences of Words in a Sentence
Write a function count_word_occurrences(sentence) that accepts a sentence and 
returns a dictionary with the count of each word in the sentence.

"""
def count_word_occurrences(sentence):
    sentence=sentence.split()
    d={}
    for i in sentence:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    return d
name='im python yas python yaya im java ok java go java god python who php haha'
print(count_word_occurrences(name))
#or
from collections import Counter
print(Counter(name.split()))