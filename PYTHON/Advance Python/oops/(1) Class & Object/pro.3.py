class just():
    def hello(self):#bina self ke error aye gi
        print("hello god mornig...")

    def name(self):
        print("mustved")
    
    def last(self):
        return "thank you."

obj=just()# bina self ke agar hum round breaket lgaye ge to error aye gi 
obj.hello()# or agar breaket nhi lgaye ge to kuch bhi print nhi hoga
obj.name()
print(obj.last())

