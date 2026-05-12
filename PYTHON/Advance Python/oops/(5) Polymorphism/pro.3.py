class A:
    def dis(self):
        # B.dis(self) agar me ye karta hu to B or A dono ka aye ga 
        print("A class")
class B:
    def dis(self):
        print("B class")
class C(A,B):
    # ya to me dono ko yha ek agal alag function me override kru fir isco call karu to hoga 
    # def dis1(self):
    #     A.dis(self)
    # def dis2(self):
    #     B.dis(self)
    pass
o=C()
o.dis()# C ke pass bhale hi dono ki property ho par same name hone ki vja se jo pehle inharit huva hoga usska hi
# ayega je se abhi A ka hi aye ga ya 
# o.dis1()