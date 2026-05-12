class A:
    def display(self):
        print(" A class is hear ...")
class B(A):# agar hum inhari na kraye to bhi hoga 
    def display(self):
        A.display(self)
        # super().display() ese bhi hoga 
        # a=A() ese bhi sem kam hi kare ga 
        # a.display()
        print(" B class is hear ...")
obj=B()
obj.display()