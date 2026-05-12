class A:
    def __init__(self):
        print("welcom to parent miting..")
class B(A):
    def disB(self):
        print("this is class B")
class C(A):
    def disC(self):
        print("this is class C")

objB=B()# child 1
objB.disB()
print("----------------------------")
objC=C()# child 2
objC.disC()
