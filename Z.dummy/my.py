import random
print("{<><><><><><><>------------+:ston,papper,sijer game:+------------<><><><><><><>}")
rols="""
                       :::rols:::
                for ston    press -> 1.
                for paper   press -> 2.
                for sijer   press -> 3.
    """
print(rols)
status=True
while status:
    computer=random.randint(1,3)
    user=int(input("enter your number :"))
    if user==computer:
        print("drow")
    elif (user==1 and computer==2) or (user==2 and computer==3) or (user==3 and computer==1):
        print("you loss~")
    elif (user==2 and computer==1) or (user==3 and computer==2) or (user==1 and computer==3):
        print("you won")
    else:
        print("\nread rool first\n")
        print(rols)
