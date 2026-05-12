class student:
    def __init__(self,n,i):
        self.name=n
        self.Id=i
    def prin_t(self):
        print("name :",self.name)
        print("ID :",self.Id)
obj=student("mustved",2)
obj.prin_t()