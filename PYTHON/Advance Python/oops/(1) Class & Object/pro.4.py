class just:
    name="mustved"
    def print_name(self):
        print("name =",self.name)
    def p_score(self):
        score=32
        print("second time name =",self.name)#name ko mai is class me khi bhi use kar skta hu
        print("score =",score)# isko me khali isi function me use kar sakta hu
    def namemo(self):# jo function uper ban gya hai usko bhi mai dobara new function me use kar sakta hu
        print(self.p_score())# function calling
#   p_score() ese call nhi kar sakta error ayegi
obj=just()
obj.print_name()
obj.namemo()
obj.p_score()
