def decorator(fun):
    def wepper():
        print('good mornig')
        fun()
        print("get reddy!!")
    return wepper
@decorator
def myfun():
    print('boss')
myfun()
#@decorator likhna matlab →myfun = decorator(myfun) automatically ho gaya!