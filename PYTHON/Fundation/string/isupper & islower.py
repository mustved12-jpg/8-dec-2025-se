name="mustved"
print(name)
name=name.isupper()
print(name)#False
#---------------------------
name="mustved12@gmail.com"#numbers or spaciell symbols meter nhi karte isme
print(name)
name=name.islower()
print(name)#True
#---------------------------
name="muSTved"
if name.islower():
    print("lower carecter.")
elif name.isupper():
    print("upper carecter.")
else:
    print("mix carecter.")