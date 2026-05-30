import re

name="198*2+3$4+5"
name1=re.split(r"[$+*]",name)
print(name1)

name="-3+3*4-5%2"
name=name[1:]
name=re.split(r"[-+*%]",name)
print(name)