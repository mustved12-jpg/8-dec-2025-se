# Q 61: Sort List of Tuples by Second Element
# Write a function sort_tuples(lst) that accepts a list of tuples, and sorts the list based on the 
# second element of each tuple in ascending order.

l1=[(3,9, 10), (8, 5), (2,7, 8),(2,5,8)]

l1.sort(key=lambda num: num[1])
# for i in range(len(l1)):
#     for j  in range(i+1,len(l1)):
#         if l1[i][1]>l1[j][1]:
#             l1[i],l1[j]=l1[j],l1[i]
print(l1)
l1=list(sorted(l1,key=lambda num: num[1]))
print(l1)