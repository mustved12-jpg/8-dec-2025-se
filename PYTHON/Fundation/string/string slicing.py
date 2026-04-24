'''
string slicing
+   0    1   2   3   4   5  (positiv index)
    p    y   t   h   o   n
-  -6   -5  -4  -3  -2  -1  (nagetiv index) isme 0 nhi hota

fetch first 2 charector fromgiving string
'''
name="pyhont"
print(name[0:3])
#or 
print(name[:3])#agar ham kuch nhi likhen ge to vo 0 hi samje ga 

# fetch last 3 chrecter
print(name[-3:-1])# ye last ka <t> nhi dikhaye ga |output: on

print(name[-3:])
# or 
size=len(name)
print(name[size-3:size])

