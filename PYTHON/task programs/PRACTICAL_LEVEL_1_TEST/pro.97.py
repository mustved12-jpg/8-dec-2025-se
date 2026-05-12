"""Q  97: Flatten a List of Lists
Write a function flatten_list_of_lists(lst) that accepts a list of lists (a nested list)
 and returns a flat list containing all the elements of the inner lists.

"""
l1=[1,2,3,[10,20],4,5,[30,40]]
def flatten_list_of_lists(lst):
    l1=[]
    for i in lst:
        if type(i)==list:
            for j in i:
                l1.append(j)
        else:
            l1.append(i)
    return l1
print(flatten_list_of_lists(l1))