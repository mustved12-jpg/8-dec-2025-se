# remove extra white space from leading and ending
name="  im mustved      "
print(name)
print(len(name))#18
print(name.strip())

name1=name.strip()
print(name1)
print(len(name1))#10

name2=name.lstrip()# remove left side space
print(name2)
print(len(name2))#16

name3=name.rstrip()# remove right side space
print(name3)
print(len(name3))#12