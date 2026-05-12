class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        print(self.name,self.id)
        # return self.name ye return nhi karta hai ye khali None ko hi return karta hai
obj=student('mustved',1)
obj.__init__('aaaa',23)#ye bhi function ki tra call hoga
