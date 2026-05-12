class A:
    def displayA(self):
        print("this is (A) class..".upper())
class B(A):
    def displayB(self):
        print("this is (B) class..".title())
obj=B()
obj.displayA()