#Q 58: Find Common Elements in Two Lists
#Write a function find_common_elements(list1, list2) that accepts two lists and returns a 
# list containing the common elements from both lists.
def find_common_elements(list1, list2):
    l3=[i for i in l1 if i in l2]
    return l3
l1=[1,2,3]
l2=[4,2,2,3,4,5,2,6]
print(find_common_elements(list1=l1,list2=l2))
