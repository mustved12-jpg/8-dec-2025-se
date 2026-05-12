class Address:
    def __init__(self,city,state,pincode):
        self.city=city
        self.state=state
        self.pincode=pincode

class employ:
    def __init__(self,name,salary,address):
        self.__name=name
        self.__salary=salary
        self.__add=address
    def dis(self):
        print("Empoy name =",self.__name)
        print("Empoy salary =",self.__salary)
        print("Empoy city =",self.__add.city)
        print("Empoy state =",self.__add.state)
        print("Empoy pincode =",self.__add.pincode)

a=Address("Ahmedabad","gujrat",6587328)
o=employ("mustved",45000,a)
o.dis()