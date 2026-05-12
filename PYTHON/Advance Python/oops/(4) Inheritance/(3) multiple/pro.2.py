class A:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def dis(self):
        print(f"{self.name}|````````|{self.id}")
class B:
    # def __init__(self):agar hum dono perent me __inti__ fanction likhen ge to jab hum A or B ko inherit
    #  karenge C me to C ke pass 2 init function honge A ke or B ke to ye method overloading ho jayega 
    # ok method over loading python me saport nhi hota hai to error ayegi
    #     self.ok="ok"  
    ok="ok"
class C(B,A):
    def __init__(self,name,id):
        super().__init__(name,id)
    def dis_A_name(self):
        print(self.name)
    def dis_B_ok(self):
        print(self.ok)

o=C("mustved",1)

o.dis()
o.dis_A_name()
o.dis_B_ok()