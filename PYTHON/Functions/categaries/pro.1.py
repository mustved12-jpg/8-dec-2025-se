def myfun():
    global name
    name+=5
    print(name)
name=10
myfun()
print(name)