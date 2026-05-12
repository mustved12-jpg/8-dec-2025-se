"""Q  100: Find the Common Keys in Two Dictionaries
Write a function find_common_keys(dict1, dict2) that accepts two dictionaries
 and returns a list of keys that appear in both dictionaries.

"""
d1={1:10,2:20,3:30}
d2={2:40,5:100,4:80,3:"mustved"}
def find_common_keys(dict1, dict2):
    l1=[i for i in dict1 if i in dict2]
    return l1
print(find_common_keys(d1,d2))