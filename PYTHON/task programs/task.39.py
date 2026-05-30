def my():
    l1=[1,2,3]
    for i in l1:
        yield i
o=my()
print(next(o))
print(next(o))
print(next(o))
o1=my()
print(next(o1))
print(next(o1))
print(next(o1))
