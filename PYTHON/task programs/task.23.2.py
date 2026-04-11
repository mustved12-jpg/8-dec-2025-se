import random
h_t=["TEAL","HEAD"]#    USER     OPP        
#                     R W O B  R W O B   /R=run,W=wicket,O=over,B=ball 
score=["SCORE BOARD",[0,0,0,0],[0,0,0,0]]
balls=[0,1,2,3,4,6,"wide ball","no ball","wicket"]
actual=random.choice(h_t)
user=input("enter your toss choice:".upper()).upper()
if ((user=="H" and actual=="HEAD") or (user=="T" and  actual=="TEAL")) or user==actual:
    print("user won the toss\n")
    bb_ch=input("enter your choice (bat/bALl) :".upper()).upper()
    if bb_ch=="BAT":
        print("bat")




    elif bb_ch=="BALL":
        print("ball")
        print("************opponet team bating first.")
        print(f"{score[0]} : oponet : {score[2][0]}/{score[2][2]}  ({score[1][2]}.{score[1][3]}) overs".upper())
        print("********************************\n")




    else:
        print("wrong input!")

elif ((user=="T" and actual=="HEAD") or (user=="H" and  actual=="TEAL")) or ((user=="HEAD" and actual=="TEAL") or(user=="TEAL" and actual=="HEAD")):
    print("oponet win")
    bb=["BALL","BAT"]
    bb_ran=random.choice(bb)
    print(f"oponent choce :{bb_ran}")
    if bb_ran=="BAT":
        print("bat")
        print("*************opponet team bating first.")
    elif bb_ran=="BALL":
        print("ball")
        print("*************user team bating first.")
    else:
        print("print wrong input!")
else:
    print("erorr")
