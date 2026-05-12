class A:
    def disA(self):
        print("A class")
class B(A):
    def disB(self):
        print("B class")
class C(B):
    def disC(self):
        print("C class")
obj=C()
obj.disA()
obj.disB()
obj.disC()