"""Q  72: Check if Two Lists are Anagrams
Write a function are_anagrams(list1, list2) that accepts two lists of strings and checks if one 
list is an anagram of the other (i.e., the lists contain the same elements, but possibly in different orders).

"""
def are_anagrams(list1, list2):
    if len(list1)==len(list2):
        for i in range(len(list1)):
            if l1[i] in l2:
                f=1
            if l2[i] in l1:
                f=1
            else:
                f=0
                break
        if f==0:
            return 'not a anagram'
        else:
            return 'anagram' 
    else:
        return 'not a anagram'.upper()

l1=['java','python','php','android']
l2=['php','android','java','python']
print(are_anagrams(l1,l2))