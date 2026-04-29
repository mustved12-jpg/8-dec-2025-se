"""Q  70: Sort Strings by Length
Write a function sort_by_length(lst) that accepts a list of strings 
and sorts the strings by their lengths in ascending order.

"""
l1=['python','java','php','androud','flutter']
l1.sort(key=lambda num: len(num))
print(l1)