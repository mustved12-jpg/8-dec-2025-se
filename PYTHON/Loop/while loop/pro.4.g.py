from enum import EnumDict
import random
print("~~~~~~~~~~~~~~:NUMBER GUESSING GAME:~~~~~~~~~~~")

computer=random.randint(1,100) # it will take rendom number from 1 to 100
print("    <.<:guess number bitween 1 to 100:>.>")
status=True
while status:
    user=int(input("enter you number =-> "))
    if user>computer:
        print("enter lower number...")
    elif user<computer:
        print("enter upper number...")
    else:
        print("<.=.+.=.> righ number <.=.+.=.>")
        status=False
