"""Q  106: Split a List into Two Lists
Write a function split_list(lst) that accepts a list and splits it into two lists.
 The first list should contain the first half of the elements, and the second list
  should contain the second half.

"""
l1=[1,2,5,3,4,5,6,6,8,8,9,12,3,4]
def split_list(lst):
    l1=[lst[i] for i in range(len(lst)//2)]
    l2=list(reversed([lst[::-1][i] for i in range(len(lst)//2)]))
    print(f"{l1}\n{l2}")
split_list(l1)