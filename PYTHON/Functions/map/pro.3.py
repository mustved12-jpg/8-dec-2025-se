# con vert into int
l1=['21','3','82','65','70','43']
def myfun(num):
    return int(num)
l2=list(map(myfun,l1))
print(f"{l1}\n{l2}")
#_____________________
l4=list(map(lambda num: int(num),l1))
print(l4)
#_________________
l3=list(map(int,l1))
print(l3)