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
        print("************usrer team bating first.")
        print(f"{score[0]} : user : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
        print("********************************\n")
        print("match stat..")
        noball=0 
        status=True
        while status:
            balling=random.choice(balls)
            input("press enter..")
            if score[2][3]==6:
                score[2][2]+=1
                score[2][3]=0


            if balling==balls[7]:   #noball
                print(f"'''''''''''''IT'S {balling}'''''''''''''''\n")
                score[1][0]+=1
                print(f"{score[0]} : user : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
                noball+=1
                print("...........free hit............")


            elif balling==balls[8]:#wicket
                print(f"'''''''''''''IT'S {balling}'''''''''''''''\n")
                if noball>=1:# ye is liye hai agar dubara out hoga to noball=0 ho gya hoga to ye yha nhi niche jayega jisme ball or wecat dono count hogi
                    print(f"{score[0]} : user : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
                    noball=0# agar me noball_l ko mines karunga to loop ki lentha kam ho jaye gi 
                else:
                    score[1][1]+=1
                    score[2][3]+=1
                    print(f"{score[0]} : user : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
                if score[1][1]>=9:
                    break


            elif balling==balls[6]:#wide ball
                print(f"'''''''''''''IT'S {balling}'''''''''''''''\n")
                score[1][0]+=1
                print(f"{score[0]} : user : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())

            elif (balling>=0 and balling<=4)or balling==6:
                print(f"'''''''''''''IT'S {balling}'''''''''''''''\n")
                if noball>=1:# ye is liye hai agar dubara out hoga to noball=0 ho gya hoga to ye yha nhi niche jayega jisme ball or wecat dono count hogi
                    score[1][0]+=balling
                    print(f"{score[0]} : user : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
                    noball=0# agar me noball_l ko mines karunga to loop ki lentha kam ho jaye gi 
                else:
                    score[1][0]+=balling
                    score[2][3]+=1
                    print(f"{score[0]} : user : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
            if score[2][2]==1 and score[2][3]==6:
                status=False 
    elif bb_ch=="BALL":
        print("ball")
        print("************opponet team bating first.")
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
