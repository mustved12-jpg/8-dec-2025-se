o=5
for i in range(1,6):
    for j in range(o,0,-1):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    for t in range(i-1):
        print("*",end="")
    print()
    o=o-1

p=2
for i in range(4,0,-1):
    for j in range(p,0,-1):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    for t in range(i-1):
        print("*",end="")
    print()
    p=p+1
