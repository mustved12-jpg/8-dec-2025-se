
class bankacount:
    def __init__(self,account,balance):
        self.acount_number=account
        self.balance=balance
    def display(self):
        print(f"{self.acount_number}<------->{self.balance}")
class saving(bankacount):
    def __init__(self,acc,bal):
        super().__init__(acc,bal)
    def withdrow(self,amount):
        self.balance-=amount
class salary(bankacount):
    def __init__(self,account,balance):
        super().__init__(account,balance)
    def deposit(self,amount):
        self.balance+=amount

savingobj=saving("211232j2j12",50000)
salaryobj=salary("dash127323",50000)

savingobj.display()
savingobj.withdrow(20000)
savingobj.display()
print("=============================")
salaryobj.display()
salaryobj.deposit(15000)
salaryobj.display()
