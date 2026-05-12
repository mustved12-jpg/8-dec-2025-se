class kuchbhi(Exception):
    pass
def myfun(num):
    if num<0:
        raise kuchbhi("negetiv number..")
    else:
        print(num)
try:
    myfun(-10)
except kuchbhi as e:
    print(e)
