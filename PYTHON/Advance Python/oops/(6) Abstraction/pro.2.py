from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def weels(self):
        pass
    @abstractmethod
    def brand(self):
        pass
class Car(A):
    def weels(self,number):
        self.__number=number
    def brand(self,name):
        self.__name=name
    def dis(self):
        print(f"car brand name = {self.__name} with {self.__number} weels...".title())
class bike (A):
    def weels(self,number):
        self.__number=number
    def brand(self,name):
        self.__name=name
    def dis(self):
        print(f"bike brand name = {self.__name} with {self.__number} weels...".title())
# class D(Car,bike):
#     def __init__(self):
#         self.nu=input("enter you choice :".upper())[0].upper()
#     def dis(self):
#         if self.nu=="Y":
#             Car.dis(self)
#         else:
#             bike.dis(self)

# o=D()
# o.weels(4)
# o.brand("tesla")
# o.dis()

C=Car()
C.weels(4)
C.brand("tesla")
C.dis()

B=bike()
B.weels(2)
B.brand("honda")
B.dis()
