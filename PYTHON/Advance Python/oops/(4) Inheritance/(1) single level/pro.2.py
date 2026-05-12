# agra hum child class me __init__() function nhi likhenge to ye arguments ko direct parent class me bhej dega
# agar humne init function liya ho ERROR ayegi
# agar me child class ke init me parameter lunga to argument child me save gogi naki parent me 
# fir agar me code runcarunga to error aye gi 


#                                               (pro.3 dekho)

class A:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def first_time(self):
        print(f"{self.name}<|----|>{self.id}")
class B(A):
    def __init__(self):
        self.ok="ok"
    def displayname(self):
        print(self.name)
    def displayid(self):
        print(self.id)
    def ch(self,name,id):
        self.name=name
        self.id=id
obj=B("mustved",123)
obj.first_time()
obj.displayname()
obj.displayid()
print("--------------------------------")
obj.ch("java",9999)
obj.first_time()
obj.displayname()
obj.displayid()