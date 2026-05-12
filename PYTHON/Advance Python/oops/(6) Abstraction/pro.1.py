from abc import ABC,abstractmethod
class parent(ABC):#iska ab me object nhi bna sakta hu
    @abstractmethod
    def property(self):
        pass#agar hum isme kuch bhi likhen ge to nhi aye ga ye is liye hai ki jise hum parent ko inharit 
    # krayenge to humho ye vali function likhna hi hoga varna error aye gi
class child1(parent):
    def property(self):
        print("i have car and bike....".title())
class child2(parent):
    def property(self):
        print("i have flat...".upper())
o1=child1()
o2=child2()
o1.property()
o2.property()