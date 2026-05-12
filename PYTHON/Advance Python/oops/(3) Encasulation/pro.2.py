class student:
    def __init__(self,name,id):
        self.name=name
        self.Id=id
    def get_id(self):
        return self.Id
    def set_id(self,id):
        self.Id=id
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
obj=student('mustved',1)
print(obj.get_name())
print(obj.get_id())
obj.set_name("python")
obj.set_id(10101)
print(obj.get_name())
print(obj.get_id())