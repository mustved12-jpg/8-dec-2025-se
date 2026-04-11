import random
menu="""
                    :MENU:
                ROCK
                PAPPER
                SCISSOR
    """

print("             welcom to the r,p,s game:\n")

rps=["ROCK","PAPPER","SCISSOR"]

status=True
while status:
    print(menu,)
    computer=random.choice(rps)
    user=input("enter your type :-").upper()#ye user jo bhi likhe ga usko upper mai convart kar dega
    print("\nuser choice:",user,)
    print("computer choice:",computer)
    if user==computer:
        print("\n===============:drow:=================\n")
    elif (computer=="ROCK" and user=="PAPPER")or(computer=="PAPPER" and user=="SCISSOR")or(computer=="SCISSOR"and user=="ROCK"):

        print("\n\\\\\\<user won>///////\n")

    elif (computer=="PAPPER" and user=="ROCK")or(computer=="SCISSOR" and user=="PAPPER")or         (computer=="ROCK"and user=="SCISSOR"):

        print("\n\\\\\\<computer won>///////\n")

    else:
        print("\nincorect details!!!\n")
    
    ch=input("do you want co continue press~> (YES) or (Y) and for exit press~> any latter :").upper()
    if ch=="YES" or ch=="Y":
        pass
    else:
        print("\n........THANK YOU FOR COMIN I HOPE YOU INJOYED......")
        status=False