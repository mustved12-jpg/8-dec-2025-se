#problem
try:#type error ayegi
    class A:
        def __init__(self,name,id):
            self.name=name
            self.id=id
        def display(salf):
            print(f"{salf.name}\t-----\t{salf.id}")
    class B(A):
        def __init__(self):# withot any parameter
            pass
        def dname(self):
            print(self.name)
        def did(self):
            print(self.id)

    obj=B("mustved",202023)#yaha se jab pass hoga to ye child me jye ga par udhar koi prameter hai nhi erroe hoga
    obj.display()
    obj.dname()
    obj.did()
except:
    pass


# ==================================== solusion 1
# class A:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def display(salf):
#         print(f"{salf.name}\t    -----\t{salf.id}")
# class B(A):
#     def __init__(self,name,id):# with parameter
# #      agar me ye karunga to ye A ke name me to chala jaye ga pr A me jo parameter hai vo koi kam ke nhi honge
#         self.name=name
#         self.id=id
#     def dname(self):
#         print(self.name)
#     def did(self):
#         print(self.id)

# obj=B("mustved",202023)
# obj.display()
# obj.dname()
# obj.did()


# ==================================== solusion 2
class A:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(salf):
        print(f"{salf.name}\t    -----\t{salf.id}")
class B(A):
    def __init__(self,name,id):
        super().__init__(name,id)
        # ^ ye jo argument B ke perameter me aye gi usko super class yani A me pass kar dega 
    # par agar me self.name="java" dunga to ye uper vala pass karne se pehle yha aye ga 
    # or name me jo bhi me pehle pass kar rha tha usko change kar ke java kar dega 
    # q ki is init ke ye constructerhe is liye ye pehle pura run goga bad me kuch bhi hoga  
    def dname(self):
        print(self.name)
    def did(self):
        print(self.id)

obj=B("mustved",202023)
obj.display()
obj.dname()
obj.did()
