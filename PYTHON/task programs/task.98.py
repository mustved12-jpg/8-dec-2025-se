# Understanding how to create and access elements in a list.
""" list creat karne ke liye sabse pehle humk list ka name = and scour[]breaket ka use karna hota hai 
fir hum usme similer or dis-similer values ko save karte hai har value ke bad koma, hota hai 
agar humko kisis soacific values ko access karna ho to hum index ka use karte hai index 2 type ke hote hai positiv or 
negetiv index positv index 0 se start hota hai or negetiv index -1 se 
"""
#Indexing in lists (positive and negative indexing).
"""
indexing matlab agar humko list me se koi spacific value ko access karna ho to hum indexing ka use karte hai isme 
positiv index or negetiv inde hota hai positiv index 0 se start hota hai righit side se or negetiv index -1 se stat 
hota hai left side se 
"""
#Slicing a list: accessing a range of elements.
"""
agar humko koch hi values ho assess karna hai sari nhi to hum list slising ka use karte hai jese ahar mujhe pehle ki
koi 2 values ko dekhna hai to main list slising ka use karunga iske syntex: ye hai ki listname[:2] to ye first 2 
values ko dikhaye ga  
"""
#Write a Python program to create a list with elements of multiple data types (integers,strings, floats, etc.).
l1=[1,"python",5.5,True]
#Write a Python program to access elements at different index positions
print(l1[0])#1
print(l1[1])#python
print(l1[2])#5.5
print(l1[3])#True

#Write a Python program to create a list of multiple data type elements.
l1=[1,"python",5.5,True,34,False,"java",98.999]
#Write a Python program to find the length of a list using the len() function.
print("lenght of list =",len(l1))
#Common list operations: concatenation, repetition, membership.
"""
jab humko do list ko concatenate karna ho to hum + pause karte hai ise hum isse hum kisi do alag alag
list ko ek me kar sakte hai iska syntax: l3=l1+l2
jab humko list ko repet karna hota hai to hum * ka use karte hai syntax: l2=l1*2 to ye 2 time repet ho jayega 
jab humko check karna ho ki hmari list me ye values hai ya nhi hum membersip ka use karte hai isme in or
not in ka use hota hai jese agar mujhe check karna ho ki "python list me hai ki nhi to mai likhunga 
if "python" in l1:   print("true") agar list me hoga to true aye ga 
"""
#Understanding list methods like append(), insert(), remove(), pop().
"""
append() method jab humko list me koi value add karna ho to hum append() method ka use karte hai but iska 
use karke hum jo bhi values ko add karenge vo liat ke last vale index pe save hoga syntax: l1.append(value)
insert() method jab humko kisi spacific index pe value ko save karna ho to hum index ka use karte hai 
syntax: l1.index(0,value)
remove() method jab humko kisi value ko delete ya remove karna ho tab hum is method ka use karte hai 
syntax: l1.remove(value)
pop() method jab humko list me se last value ya kisi spacific index ki value ko delete karna ho tab hum is 
method ka use karte hai syntax: l1.pop() ye last vali value ko dilete kare ga l1.pop(2) ye 2 number index 
vali value ko delete karega 
"""
#Write a Python program to add elements to a list using insert() and append().
l1=[]#bnak list
l1.append(100)
l1.append("python")
l1.append(True)
print(l1[0])#100
l1.insert(0,'java')
print(l1[0])#java
#Write a Python program to remove elements from a list using pop() and remove().
l1.remove('java')
print(l1[0])#100
print(l1[-1])#True
l1.pop()
print(l1[-1])#python
l1.pop(0)
#now list is blank
#Iterating over a list using loops.
"""
lopp ka use kar ke hum list ke sare eliment ko one by one access kar sakte hai 
"""
#Sorting and reversing a list using sort(), sorted(), and reverse()
"""
sort() method ka use karke hum values ko accending ya diccending mai kar sakte hai isse acchoal list me changes hote hai 
sort() method ko hum direct dusre vareable me use nhi kar sakte hai 
sorted() function ka use kar ke hum humlist ko accending ya diccending kar kar sakte hai or hum ek list ko dusti men
save bhi kar sakte hai 
reverse() method ka use kar ke hum list vo revers kar sakte hai ye bhi direct orijnal list ko hi revers karta hai 
revers() method ko hum direct dusre vareable me use nhi kar sakte hai 
"""
#Basic list manipulations: addition, deletion, updating, and slicing.
"""
addition mai hum list ke ander values ya eliment ko add karte hai 
iske 3 method hai 1 append() 2 extend() 3 insert()
deletion mai hum list me jo value ya eliment usko delete karte hai 
iske 3 method or ek keword hai 1 remove() 2 pop() 3 clear() 4 is datatype del
updating mai agar humko koi value ya eliment change karna ho to hum updating ka use karte hai
e.g agar meri list me 0 index position pe 10 hai or mujhe usko 20 karna ho tab hum updating karte hai l1[0]=20
slicing agar mujhe kuch hi values ko access karna ho tab mai slicing ka usekarunga jese agr mujhe pehle ki rirf do elimnet
ka kam ho to mai slising ka use karke un dono ko access kar sakta hu
"""
# Write a Python program to iterate over a list using a for loop.
l1=[1,2,3,10,5,40,52,6,7,4,8,9,98.999]
for i in l1:
    print(i)

#Write a Python program to sort a list using both sort() and sorted().
# using sorted()
l2=list(sorted(l1))
print(l1)
print(l2)
#now sort()
l1.sort()
print(l1)
#Write a Python program to insert elements into an empty list using a for loop and append().
l1=[]
print(l1)
for i in range(1,6):
    l1.append(i)
print(l1)
#Introduction to tuples, immutability.
"""
tuple list ki tra hi hoti ordreble indexible secounced but ye immuteble ho ti hai ek bar taple banne ke bad hum usme 
koi bhi changes nhi kar sakte hai like add delete ya update.
"""
#Creating and accessing elements in a tuple
"""
taple creat karne ke liye humko sab se pehle table ka variable name likhna hoga fir = and fir round breaket is round
breaket mai hum eliment ko rakhenge eliment ko access karne ke liye hum index ka use karenge isme bhi positiv or negetiv
indexing hot hai 
"""
#Basic operations with tuples: concatenation, repetition, membership
"""
jab humko do tuple ko concatenate karna ho to hum + pause karte hai ise hum isse hum kisi do alag alag
tuple ko ek me kar sakte hai iska syntax: t3=t1+t2
jab humko tuple ko repet karna hota hai to hum * ka use karte hai syntax: t2=t1*2 to ye 2 time repet ho jayega 
jab humko check karna ho ki hmari tuple me ye values hai ya nhi hum membersip ka use karte hai isme in or
not in ka use hota hai jese agar mujhe check karna ho ki "python tuple me hai ki nhi to mai likhunga 
if "python" in t1:   print("true") agar tuple me hoga to true aye ga 
"""
#Write a Python program to create a tuple with multiple data types.
t1=(1,'python',54.55,6,True)
# Write a Python program to concatenate two tuples.
t2=(2,"java",False,9.99)
t3=t1+t2
print(t3)
#Write a Python program to convert a list into a tuple. 
l1=[1,2,3,10,5,40,52,6,7,4,8,9,98.999]
t1=tuple(l1)
print(t1)
#Write a Python program to access the value of the first index in a tuple.
t=('mustved',1,4.76,True)
print(t[0])

#Accessing tuple elements using positive and negative indexing.
"""
tumple me bhi positiv index ho ti hai or negetiv index positiv index right se 0 se start hoti hai or 1+ hoti hai 
or negetiv index left -1 se start horta hai or 1- hota hai 
"""
# Write a Python program to access values between index 1 and 5 in a tuple.
t1=(1,2,3,4,5,6,7,8,9,10)
print(t1[1:6])
print(t1[1:6:2])
#Write a Python program to access the value from the last index in a tuple.
print(t1[-1])
#Introduction to dictionaries: key-value pairs.
"""
dictionary coleection ka ek data type hai isme key and values ek jodi me hoti hai key means index
dictionary muteble hoti hai ordreble hoti hai but isme hum keys ko change ya replace nhi kar sakte hai
dictionry represent by {} breaks and similer keys nhi ho ssakti kes unique ho ni chahiye 
"""
#Accessing, adding, updating, and deleting dictionary elements.
"""
accessing dictionary ki kisi bhi value ko access karne ke liye key ka use hota hai jis value ko humko access karna
hai uski key se hum usko access kar sakte hai
aading mai hum agar hmari dictionary mai hum jo bhi key add karen ge vo dictionary me nhi honi chaye 
syntax: dictionary name['keyname']=value
dileting humko jo  bhi value ko delete karna hai hum uski key ko pop(key) me likhenge isse key and value dono delete
ho jaye gi hum khali key ya khali value ko nhi delete kar sakte q ki dono jodi hoti hai 
"""
#Dictionary methods like keys(), values(), and items().
"""
wen we use key() metoud we can access only key and usnig of values() we can access only value and using of
item() method we can access key and value both
"""
# Write a Python program to create a dictionary with 6 key-value pairs.
d={'name1':'mustved','name2':'aaaaa','name3':'bbbbb','name4':'cccccc','name5':'ddddd','name6':'eeeee'}
print(d)
#Write a Python program to access values using dictionary keys.
print(d['name1'])
print(d['name4'])
#Iterating over a dictionary using loops.
"""
agar humko dictionary ke sare eliments ko one by one access karna ho to hum for loop ka use kar ke intraot 
kar sakte hai
"""
#Merging two lists into a dictionary using loops or zip().
"""
zip function ka use kar ke hum do one list me convert kar sakte hai concatinaion me bhi yhi hota hai par 
usme pehli list ki vale save hoti hai fir dusri list ki valie but zip me esa nhi hota isme ek value l1 to 
dusri value l2 ki save hogi 
"""
#Write a Python program to update a value in a dictionary.
d={'name':'aaaa'}
print(d)
d['name']='mustved'
print(d)
#Write a Python program to merge two lists into one dictionary using a loop
roll=[1,2,3,4]
name=['mustved','aaaa','bbbb','cccc']
d={}
for i in range(len(roll)):
    d[roll[i]]=name[i]

print(d)
#Defining functions in Python.
"""
function ek block of code hota hai jisko ek bar likhne se hum bar bar use kar sakte hai isse hmara code
chota hota hai or agar koi bug hota hai to humko pura code fir se dekhne ki jarorat nhi hoti hai hum bus
usi function ke kode ko dekh ke bug fix kar sakte hai function ka use karke hmara time bachta hai
functio ko bnane ke liye dif keyword ka use karte hai 
function ki 4 ccategory hoti hai 
functio 1.np nr 2.np wr 3.wp nr 4.wp wr
function 2 type ke hote hao
1>inbuiltd function jo inbuilt hote hai jese print(),input(),len(),max etc.
2>user difined function ye user creat karta hai apni jrurat ke hisab se 
"""
# Different types of functions: with/without parameters, with/without return values.
"""
without parameter mai hum koi bhi argumnet pass nhi karte hai to hum jo bhi value function ke ander lete hai
vo bus function me hi hoti hai hum uska use nhi kar sakte with me paramenter me hum jo bhi argument pass karte
hai vo function me use hoti hai 
without return me hum function me se kuch bhi return nhi krate hai and with return me hum jese humko function
ki kisi value ko use karna hai function ke bahar to hum usko return kra ke use kar sakte hai
"""
#Anonymous functions (lambda functions).
"""
jis function ka koi bhi name nhi hota hai vo anonymous function (lambda) hot hai isko ham lambda keyword
ka use kar ke create kar sakte hai isme khali ek exprestion accept hota hai ye result ko autometic return 
karta hai humko return likhne ki jarurat nhi hoti hai isme multiple parameter ho sakte hai
"""
# Write a Python program to create a function that takes a string as input and prints it.
def myfun():
    name=input("enter your name :")
    print(name)
myfun()
#Write a Python program to create a calculator using functions.
def plus(num1,num2):
    num3=num1+num2
    return num3
def minus(num1,num2):
    num3=num1-num2
    return num3
def mul(num1,num2):
    num3=num1*num2
    return num3
def div(num1,num2):
    num3=num1/num2
    return num3
print(f"{plus(5,2)}\n{minus(8,4)}\n{mul(2,6)}\n{div(10,2)}")