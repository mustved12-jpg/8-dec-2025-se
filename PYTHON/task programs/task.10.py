import random
menu="""
                MENU:
                =-> ROCK
                =-> PAPPER
                =-> SCISSOR
    """
d=0
u=0
c=0
u_name="mustved"
demo=["ROCK","PAPPER","SCISSOR"]
status=True

while status:
    computer=random.choice(demo)
    print(menu,)
    user=input("enter you choice :").upper()
    print("computer choice =~>",computer)
    print(f"{u_name} choice =~> {user}\n")
    if computer==user:
        print("<><><><><><><><>:drow:<><><><><><><><><><>")
        d+=1
    elif (computer=="ROCK" and user=="PAPPER")or(computer=="PAPPER" and user=="SCISSOR")or(computer=="SCISSOR"and user=="ROCK"):
        print(f"\\\\\\<{u_name} won>///////")
        u+=1
    elif (computer=="PAPPER" and user=="ROCK")or(computer=="SCISSOR" and user=="PAPPER")or(computer=="ROCK"and user=="SCISSOR"):
        print("\\\\\\<computer won>///////")
        c+=1
    else:
        print("incorect details!!!")
    
    choice=input("\ndo you want t continue PRESS~> YES (Y) OR ~> PRESS NO (N):").upper()
    if choice=="YES" or choice=="Y":
        print()    
    else:
        print(f"computer win {c} time.")
        print(f"{u_name} win {u} time.")
        print(f"drow {d} time.")
        status=False




