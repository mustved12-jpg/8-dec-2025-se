num=0
def ok(fun):
    def weper():
        if num==1:
            print("ok")
        else:
            fun("pp")
    return weper
@ok
def my(num):
    print("my =",num)
# name=ok(my)
my()
num=1
my()


