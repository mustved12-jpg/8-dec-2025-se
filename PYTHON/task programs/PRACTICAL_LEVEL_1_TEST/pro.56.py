#Q 56: Count Words in a Sentence :Write a function count_words(sentence) that accepts a 
# sentence and returns the number of words in the sentence.
def count_words(sentence):
    sentence=len(sentence.split())
    return sentence
name='im mustved and im python developer'
print(count_words(name))