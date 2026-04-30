f=open("my file 1.txt")
print(f.read())
f.close()
#or 
print("-------------------")
f=open("my file 1.txt","r")
print(f.read())
f.close()

# agar humko line by line print krana ho tab hum
print("-------------------")
f=open('my file 1.txt','r')
print(f.readline())
print(f.readline(6))# agar me isme 6 likhunga to to 2 line ka bus 6 words hi ayege
print(f.readline())#baki ke idhar aye ge yani next  line me
print(f.readline())
print(f.readline())# agar line hogi to aye gi varna kuch nhi ayega blank
f.close() 

# agra humko dekhna ho ki kitni line hai hmare pass to hum readlines ka use kar sakte hai
# ye sari lines ko list ke form me dikhata hai
print("-------------------")
f=open('my file 1.txt','r')
print(f.readlines())
print(f.readlines())# ek bar humne data yni lines nhila liya to dubara usko nhi nikal sakte
# agar dubara nikalna ho to new  vareable me file ko save karna hoga
f11=open('my file 1.txt','r')
print("total lines =",len(f11.readlines()))
f.close()
f11.close()

# agar humko sirf dusri line  hi print karna ho tab
print("-------------------")
f=open('my file 1.txt','r')
print(f.readlines()[1])# to ye dusri line print kare ga q ki dusri line 1 index pe hai
f.close()