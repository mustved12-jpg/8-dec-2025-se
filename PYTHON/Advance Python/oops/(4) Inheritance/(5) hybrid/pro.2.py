class A:
    def __init__(self,name,id,cname):
        self.name=name
        self.id=id
        self.Cname=cname
    def display(self):
        print(f"{self.name}<_____________>{self.id}")
class B(A):
    def __init__(self,name,id,cname,Bname):
        super().__init__(name,id,cname)
        self.Bname=Bname
    def disB(self):
        print(self.Bname)
class C(A):
    # me idhar INIT method nhi likh sakta hu q ki jab me B or C ko D me inharit karunga to overloding hoga error
    def disC(self):
        print(self.Cname)
class D(B,C):
    def All(self):
        print("All propertys..")

obj=D("mustevd",1,"Cname is hello","B name is nikallo") 
obj.display()
obj.disB()
obj.disC()  