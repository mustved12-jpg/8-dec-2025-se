'''
print output using all types format function/string function

'''
name=input("enter your name :")
score=int(input("enter your score :"))
pri=float(input("enter price :"))

print("datatype :",type(name),type(pri))
print("address of pri =",id(pri))

print("name =",name,"and score is =",score,"and price =",pri)
print(f"name = {name} and score is = {score} and price = {pri}")
print("name = {0} and score is = {2} and price = {1}".format(name,pri,score))