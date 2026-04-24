#zip function which is used to combine multiple list into single entity

l1=['pizza','pasta','borger']
l2=[199,100,49,80]
# 80 number match nhi hoga to zip isko skip kar dega 
l3=dict(zip(l1,l2))
print(l3)
#dictionry me direct unzip nhi hoga
l4=[(k,v) for k,v in l3.items()]
print(l4)
l5,l6=zip(*l4)
print(f"{l5}\n{l6}")