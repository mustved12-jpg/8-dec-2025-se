class A:
    def dis(self):
        print("im mustved")
class B:
    def __init__(self,a):
        self.__Aclass=a
    def ok(self):
        self.__Aclass.dis()
a=A()
o=B(a)
o.ok()
# bina inharit kiye dusre class ki pro perty ko access karna 