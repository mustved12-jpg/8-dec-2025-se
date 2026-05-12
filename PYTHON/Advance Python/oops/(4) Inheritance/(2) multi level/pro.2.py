class A:
    def __init__(salf,name,id):
        salf.name=name
        salf.id=id
    def dis(self):
        print(self.name,end="\t------------\t")
        print(self.id)

class B(A):
    def __init__(self,name1,id1):
        # super().__init__(name1,id1)# ye bheje ga A me 
        pass
    def dis_in_B_name(self):
        print(self.name)
    def dis_in_B_id(self):
        print(self.id)

class C(B):
    def __init__(self,name2,id2):
        # super().__init__(name2,id2)# ye bheje ga B me 

        self.name=name2     #bina super ka use kare
        self.id=id2       # isse hum direct A me bhej sakte hai


    def dis_in_C_name(self):
        print(self.name)
    def dis_in_C_id(self):
        print(self.id)

o=C('mustved',37432)
o.dis()
o.dis_in_B_name()
o.dis_in_B_id()
o.dis_in_C_name()
o.dis_in_C_id()