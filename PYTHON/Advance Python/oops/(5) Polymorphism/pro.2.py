try:
    class A:
        def __init__(self,name1,id1):
            self.name1=name1
            self.id1=id1
        def dis(self):
            print("Name1 :",self.name1)
            print("Id1 :",self.id1)
    class B:# humne inherit nhi kiya hai to argument A me jaye gi nhi to value print bhi nhi hogi
        def dis(self):
            A.dis(self) #error ayegi
            print("ok")

    obj=B()
    obj.dis()
except:
    class A:
        def __init__(self,name1,id1):
            self.name1=name1
            self.id1=id1
        def dis(self):
            print("Name1 :",self.name1)
            print("Id1 :",self.id1)
    class B(A):# ya to inharit kra ke kar sakte hai ys to A ka yha object pna ke usme value pass kar sakte hai
        def __init__(self,name,id):
            super().__init__(name,id)
        def dis(self):
            A.dis(self)
            print("ok")

    obj=B("mustved",1976)
    obj.dis()