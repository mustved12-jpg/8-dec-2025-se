# Q 64: Merge Two Lists Alternately
# Write a function merge_alternate(list1, list2) that accepts two lists of the same length 
# and returns a new list by merging them alternately.
# def merge_alternate(list1, list2):
#     l3=list(zip(list1,list2))
#     l4=[]
#     for i in l3:
#         for j in i:
#             l4.append(j)
#     return l4
# l1=[1,2,3]
# l2=[4,5,6]
# print(merge_alternate(l1,l2))

# #or
def my(n1,n2):
    l3=[]
    for i in range(len(n1)):
        l3.extend([n1[i],n2[i]])
    return l3

l1=[1,2,3]
l2=[4,5,6]
print(my(l1,l2))