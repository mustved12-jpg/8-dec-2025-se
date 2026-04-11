#===============================================:alpha:====================================================
                                            #  isalpha()
name="mustved"
print(name)
print(name.isalpha())#true
#--------------------------------------
name="mustved12@gmail.com"# ye khali alphabet ko hi tru btata hai bali sab false
print(name)
print(name.isalpha())#false
#--------------------------------------

name=input("enter your name:").isalpha()
print(name)#true or false
print("=======================================")
#=================================================:numbers:==================================================
                                            #   isnumeric()
# sem hai bus vo alphabet hai ye number hai
number="12345123"
print(number)
print(number.isnumeric())#true
#--------------------------------------
number="12-3-45_672"# ye khali positiv numbers ko hi tru btata hai bali sab false
print(number)
print(number.isnumeric())#false
#--------------------------------------

number=input("enter your number:").isnumeric()
print(number)#true or false

print("-----------------------------------")

name=input("enter a name:".upper())
if name.isalpha():
    print("name is alpha=",name)
elif name.isnumeric():
    print("name is numbers=",name)
else:
    print("mix name.")

#=======================================================:both:=========================================
                                                    #isalnum()
#both numbers and alpha no special symbols

name1="mustved"
name2="123456"
name3="mustved123212"
name4="mustved 12"
name5="mustved12@"
print(name1.isalpha())#True
print(name2.isalnum())#True
print(name3.isalnum())#True
print(name4.isalnum())#False
print(name5.isalnum())#False
