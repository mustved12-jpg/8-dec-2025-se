#zip function which is used to combine multiple list into single entity

l1=['pizza','pasta','borger']
l2=[199,100,49,80]
# 80 number match nhi hoga to zip isko skip kar dega 
l3=list(zip(l1,l2))
print(l3)

#unzip is a opposite preocess of zip function and ther is no such keyword like unzip

l4,l5=zip(*l3)
l4=list(l4)
print(l4)
print(l5)