"""Q  73: Flatten a Nested List
Write a function flatten_list(nested_list) that accepts a 
nested list (list containing other lists) and returns a flat list containing all the elements.

"""
def flatten_list(nested_list):
    lis=[]
    for i in nested_list:
        if type(i)==list:
            for j in i:
                lis.append(j)
        else:
            lis.append(i)
    return lis
print(flatten_list([1,2,3,[4,5,6],7,8]))