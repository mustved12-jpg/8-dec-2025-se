class just:
    def __init__(self,name,id):
        self.name=name
        self.__id=id
    def myfun(self):
        print(self.name)
        print(self.__id)
obj=just("mustved",1010)
obj.myfun()
print(obj.name)
# print(obj.__id) ERROR aye gi q ki id private hai isko khali usi class me use kar sakta hu 