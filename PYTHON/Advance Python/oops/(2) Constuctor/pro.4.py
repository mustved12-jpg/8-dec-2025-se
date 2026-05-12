class distruction:
    def __init__(self):
        self.name='mustved'
        self.id=1
    def myfun(self):
        print('Name :',self.name)
        print('ID :',self.id)
    def ok(self):
        self.name='java'
    def __del__(self):
        print("end of this object or progarm....")
obj=distruction()
obj.myfun()
print(obj.name)
obj.ok()
# jab tak me jisme name change kiya hu usko call nhi karun ga tab tak name me 'mustved' hi rhe ga abhi chang ho gya
print(obj.name)
del obj
# de vala function call karne ke bad ye object delete ho jaye ga fir is obj se hum or kuch bhi call nhi kar sakte
#agar fir kuch call karna hai to new object bnana hoga