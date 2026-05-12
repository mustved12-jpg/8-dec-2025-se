class vehicle:
    def info(self):
        print("this is info about vehicle...".title())                         # vehicle
class car(vehicle):                                                         #       |
    def car(self):                                                   #     ----------------------
        print("info mation about car..")                            #      |                    |
class Ecar(vehicle):                                                #    car                 ecar
    def ecar(self):                                                 #     |                   |
        print("info mation about E-car..")                          #     ---------------------
class tesla(car,Ecar):                                              #               |
    def display(self):                                              #             tesla
        print("we have both...")

obj=tesla()
obj.info()
obj.car()
obj.ecar()
obj.display()
