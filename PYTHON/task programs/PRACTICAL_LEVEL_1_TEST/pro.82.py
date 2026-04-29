"""Q  82: Check if Two Strings are Anagrams
Write a function is_anagram(str1, str2) that accepts two strings and 
checks if they are anagrams of each other (i.e., they contain the same characters in different orders).

"""
def is_anagram(str1, str2):
    if len(str1)==len(str2):
        for i in range(len(str1)):
            if str1[i] in str2:
                f=1
            else:
                f=0
                break
            if  str2[i] in str1:
                f=1
            else:
                f=0
                break
        if f==1:
            return 'anagram'.upper()
        else:
            return 'not a anagram'.upper()
    else:
        return 'not a anagram'.upper()
print(is_anagram('mustved','tmveusd'))
