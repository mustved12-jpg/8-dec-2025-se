# Q 20: Write a function that accepts a list of strings and returns a new list with only the strings that have an odd length.
def myfun(li):
    l2=[i for i in li if len(i)%2!=0]
    return l2
l1=['java','python','php','mustved','flutter','android']
print(myfun(l1))