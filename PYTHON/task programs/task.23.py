import random
l1=["CSK","MI","GT","RR","RCB","KKR"]
h_t=["TEAL","HEAD"]#    USER     OPP    
#                     R W O B   R W O B   /R=run,W=wicket,O=over,B=ball 
score=["SCORE BOARD",[0,0,0,0],[0,0,0,0]]
balls=[0,1,2,3,4,6,"wide ball","no ball","wicket"]
for i in range(len(l1)):
    if i==0:
        print("\n\n\n\t  -----------------:IPL 2026 :-------------------")
    print(f"\t  ({l1[i]})",end="")
print("\n")
t=True

team=input("enter your team name :".upper()).upper()

if team not in l1:
    print("!!!wrong team name!!!".upper())
elif team in l1:
    l1.remove(team)
    opp=random.choice(l1)
    print(f"oppnet team : {opp}".upper())
    print("__________________________________________\nTOSS TIME:\n")
    print("\t H/T\n")
    actual=random.choice(h_t)
    user=input("enter your toss choice:".upper()).upper()
    if ((user=="H" and actual=="HEAD") or (user=="T" and  actual=="TEAL")) or user==actual:
        print(f"~~~~~~~~~~~~~~~~':{team} won the toss:'~~~~~~~~~~~~~~~~~~~~~~\n")
        bb_ch=input("enter your choice (bat/bALl) :".upper()).upper()
        if bb_ch=="BAT":
            print(f"\n\t\t<<<<<<<<<<<<({team}: first bating)>>>>>>>>>>>>>>>>>\n")
            print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
            print("\n\t\t*********************************************\n")
            noball=0 
            while t:
                balling=random.choice(balls)
                input("\n\t~.^.~.^.~.^.~.^.~.^.~.^.~:press enter:<o_o>")
                if score[2][3]==6:
                    score[2][2]+=1
                    score[2][3]=0

                if balling==balls[7]:   #noball
                    print(f"\n\t\t''''''''''''':It's  <^_^> {balling.upper()}:'''''''''''''''\n")
                    score[1][0]+=1
                    print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
                    noball+=1
                    print("\t\t[[[[]]]]...:Freeeeeeee Hiiiittttt:...[[[[]]]]\n")
#----------------------------------------------------------------------------------------------------------------------------------
                elif balling==balls[8]:#wicket
                    print(f"\n\t\t'''''''''''''It's {balling}'''''''''''''''\n")
                    if noball>=1:# ye is liye hai agar dubara out hoga to noball=0 ho gya hoga to ye yha nhi niche jayega jisme ball or wecat dono count hogi
                        print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
                        noball=0# agar me noball_l ko mines karunga to loop ki lentha kam ho jaye gi 
                    else:
                        score[1][1]+=1
                        score[2][3]+=1
                        print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
                    if score[1][1]>=9:
                        break
#------------------------------------------------------------------------------------------------------------------------------------
                elif balling==balls[6]:#wide ball
                    print(f"\n\t\t'''''''''''''It's {balling}'''''''''''''''\n")
                    score[1][0]+=1
                    print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
#------------------------------------------------------------------------------------------------------------------------------------
                elif (balling>=0 and balling<=4)or balling==6:
                    print(f"\n\t\t'''''''''''''It's {balling}'''''''''''''''\n")
                    if noball>=1:# ye is liye hai agar dubara out hoga to noball=0 ho gya hoga to ye yha nhi niche jayega jisme ball or wecat dono count hogi
                        score[1][0]+=balling
                        print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
                        noball=0# agar me noball_l ko mines karunga to loop ki lentha kam ho jaye gi 
                    else:
                        score[1][0]+=balling
                        score[2][3]+=1
                        print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
#------------------------------------------------------------------------------------------------------------------------------------
                if score[2][2]==1 and score[2][3]==6:
                    print("\t############################################################################################################################")
                    print(f"\n\t\t\t\toooooooooooo[[[{team} score =-> {score[1][0]}]]]oooooooooooooooo\n\n")
                    t=False
#``````````````````````````````````````bating end
        
        elif bb_ch=="BALL":
            print(f"************{opp} team bating first.")
            print(f"\t\t{score[0]} : {opp} : {score[2][0]}/{score[2][1]}  ({score[1][2]}.{score[1][3]}) overs".upper())
            print("\n\t\t*********************************************\n")
            noball=0
            while t:
                balling=random.choice(balls)
                input("\n\t~.^.~.^.~.^.~.^.~.^.~.^.~:press enter:<o_o>")
                if score[1][3]==6:
                    score[1][2]+=1
                    score[1][3]=0

                if balling==balls[7]:   #noball
                    print(f"\n\t\t''''''''''''':It's  <^_^> {balling.upper()}:'''''''''''''''\n")
                    score[2][0]+=1
                    print(f"\t\t{score[0]} : {opp} : {score[2][0]}/{score[2][1]}  ({score[1][2]}.{score[1][3]}) overs".upper())
                    noball+=1
                    print("\t\t[[[[]]]]...:Freeeeeeee Hiiiittttt:...[[[[]]]]\n")
#----------------------------------------------------------------------------------------------------------------------------------
                elif balling==balls[8]:#wicket
                    print(f"\n\t\t'''''''''''''It's {balling}'''''''''''''''\n")
                    if noball>=1:# ye is liye hai agar dubara out hoga to noball=0 ho gya hoga to ye yha nhi niche jayega jisme ball or wecat dono count hogi
                        print(f"\t\t{score[0]} : {opp} : {score[2][0]}/{score[2][1]}  ({score[1][2]}.{score[1][3]}) overs".upper())
                        noball=0# agar me noball_l ko mines karunga to loop ki lentha kam ho jaye gi 
                    else:
                        score[2][1]+=1
                        score[1][3]+=1
                        print(f"\t\t{score[0]} : {opp} : {score[2][0]}/{score[2][1]}  ({score[1][2]}.{score[1][3]}) overs".upper())
                    if score[2][1]>=9:
                        break
#------------------------------------------------------------------------------------------------------------------------------------
                elif balling==balls[6]:#wide ball
                    print(f"\n\t\t'''''''''''''It's {balling}'''''''''''''''\n")
                    score[2][0]+=1
                    print(f"\t\t{score[0]} : {opp} : {score[2][0]}/{score[2][1]}  ({score[1][2]}.{score[1][3]}) overs".upper())
#------------------------------------------------------------------------------------------------------------------------------------
                elif (balling>=0 and balling<=4)or balling==6:
                    print(f"\n\t\t'''''''''''''It's {balling}'''''''''''''''\n")
                    if noball>=1:# ye is liye hai agar dubara out hoga to noball=0 ho gya hoga to ye yha nhi niche jayega jisme ball or wecat dono count hogi
                        score[2][0]+=balling
                        print(f"\t\t{score[0]} : {opp} : {score[2][0]}/{score[2][1]}  ({score[1][2]}.{score[1][3]}) overs".upper())
                        noball=0# agar me noball_l ko mines karunga to loop ki lentha kam ho jaye gi 
                    else:
                        score[2][0]+=balling
                        score[1][3]+=1
                        print(f"\t\t{score[0]} : {opp} : {score[2][0]}/{score[2][1]}  ({score[1][2]}.{score[1][3]}) overs".upper())
#------------------------------------------------------------------------------------------------------------------------------------
                if score[1][2]==1 and score[1][3]==6:
                    print("\t############################################################################################################################")
                    print(f"\n\t\t\t\toooooooooooo[[[{opp} score =-> {score[2][0]}]]]oooooooooooooooo\n\n")
                    t=False
#----------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------balling end
        else:
            print("wrong input!")
#~~~~~~~~~~~~~~~~~toss win end hear

    elif ((user=="T" and actual=="HEAD") or (user=="H" and  actual=="TEAL")) or ((user=="HEAD" and actual=="TEAL") or(user=="TEAL" and actual=="HEAD")):
        bb=["BALL","BAT"]
        bb_ran=random.choice(bb)
        print(f"oponent choce :{bb_ran}")
        if bb_ran=="BAT":
            print(f"************{opp} team bating first.")
            print(f"\t\t{score[0]} : {opp} : {score[2][0]}/{score[2][1]}  ({score[1][2]}.{score[1][3]}) overs".upper())
            print("\n\t\t*********************************************\n")
            noball=0
            while t:
                balling=random.choice(balls)
                input("\n\t~.^.~.^.~.^.~.^.~.^.~.^.~:press enter:<o_o>")
                if score[1][3]==6:
                    score[1][2]+=1
                    score[1][3]=0

                if balling==balls[7]:   #noball
                    print(f"\n\t\t''''''''''''':It's  <^_^> {balling.upper()}:'''''''''''''''\n")
                    score[2][0]+=1
                    print(f"\t\t{score[0]} : {opp} : {score[2][0]}/{score[2][1]}  ({score[1][2]}.{score[1][3]}) overs".upper())
                    noball+=1
                    print("\t\t[[[[]]]]...:Freeeeeeee Hiiiittttt:...[[[[]]]]\n")
#----------------------------------------------------------------------------------------------------------------------------------
                elif balling==balls[8]:#wicket
                    print(f"\n\t\t'''''''''''''It's {balling}'''''''''''''''\n")
                    if noball>=1:# ye is liye hai agar dubara out hoga to noball=0 ho gya hoga to ye yha nhi niche jayega jisme ball or wecat dono count hogi
                        print(f"\t\t{score[0]} : {opp} : {score[2][0]}/{score[2][1]}  ({score[1][2]}.{score[1][3]}) overs".upper())
                        noball=0# agar me noball_l ko mines karunga to loop ki lentha kam ho jaye gi 
                    else:
                        score[2][1]+=1
                        score[1][3]+=1
                        print(f"\t\t{score[0]} : {opp} : {score[2][0]}/{score[2][1]}  ({score[1][2]}.{score[1][3]}) overs".upper())
                    if score[2][1]>=9:
                        break
#------------------------------------------------------------------------------------------------------------------------------------
                elif balling==balls[6]:#wide ball
                    print(f"\n\t\t'''''''''''''It's {balling}'''''''''''''''\n")
                    score[2][0]+=1
                    print(f"\t\t{score[0]} : {opp} : {score[2][0]}/{score[2][1]}  ({score[1][2]}.{score[1][3]}) overs".upper())
#------------------------------------------------------------------------------------------------------------------------------------
                elif (balling>=0 and balling<=4)or balling==6:
                    print(f"\n\t\t'''''''''''''It's {balling}'''''''''''''''\n")
                    if noball>=1:# ye is liye hai agar dubara out hoga to noball=0 ho gya hoga to ye yha nhi niche jayega jisme ball or wecat dono count hogi
                        score[2][0]+=balling
                        print(f"\t\t{score[0]} : {opp} : {score[2][0]}/{score[2][1]}  ({score[1][2]}.{score[1][3]}) overs".upper())
                        noball=0# agar me noball_l ko mines karunga to loop ki lentha kam ho jaye gi 
                    else:
                        score[2][0]+=balling
                        score[1][3]+=1
                        print(f"\t\t{score[0]} : {opp} : {score[2][0]}/{score[2][1]}  ({score[1][2]}.{score[1][3]}) overs".upper())
#------------------------------------------------------------------------------------------------------------------------------------
                if score[1][2]==1 and score[1][3]==6:
                    print("\t############################################################################################################################")
                    print(f"\n\t\t\t\toooooooooooo[[[{opp} score =-> {score[2][0]}]]]oooooooooooooooo\n\n")
                    t=False
            
        elif bb_ran=="BALL":
            print(f"\n\t\t<<<<<<<<<<<<({team}: first bating)>>>>>>>>>>>>>>>>>\n")
            print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
            print("\n\t\t*********************************************\n")
            noball=0 
            while t:
                balling=random.choice(balls)
                input("\n\t~.^.~.^.~.^.~.^.~.^.~.^.~:press enter:<o_o>")
                if score[2][3]==6:
                    score[2][2]+=1
                    score[2][3]=0

                if balling==balls[7]:   #noball
                    print(f"\n\t\t''''''''''''':It's  <^_^> {balling.upper()}:'''''''''''''''\n")
                    score[1][0]+=1
                    print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
                    noball+=1
                    print("\t\t[[[[]]]]...:Freeeeeeee Hiiiittttt:...[[[[]]]]\n")
#----------------------------------------------------------------------------------------------------------------------------------
                elif balling==balls[8]:#wicket
                    print(f"\n\t\t'''''''''''''It's {balling}'''''''''''''''\n")
                    if noball>=1:# ye is liye hai agar dubara out hoga to noball=0 ho gya hoga to ye yha nhi niche jayega jisme ball or wecat dono count hogi
                        print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
                        noball=0# agar me noball_l ko mines karunga to loop ki lentha kam ho jaye gi 
                    else:
                        score[1][1]+=1
                        score[2][3]+=1
                        print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
                    if score[1][1]>=9:
                        break
#------------------------------------------------------------------------------------------------------------------------------------
                elif balling==balls[6]:#wide ball
                    print(f"\n\t\t'''''''''''''It's {balling}'''''''''''''''\n")
                    score[1][0]+=1
                    print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
#------------------------------------------------------------------------------------------------------------------------------------
                elif (balling>=0 and balling<=4)or balling==6:
                    print(f"\n\t\t'''''''''''''It's {balling}'''''''''''''''\n")
                    if noball>=1:# ye is liye hai agar dubara out hoga to noball=0 ho gya hoga to ye yha nhi niche jayega jisme ball or wecat dono count hogi
                        score[1][0]+=balling
                        print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
                        noball=0# agar me noball_l ko mines karunga to loop ki lentha kam ho jaye gi 
                    else:
                        score[1][0]+=balling
                        score[2][3]+=1
                        print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
#------------------------------------------------------------------------------------------------------------------------------------
                if score[2][2]==1 and score[2][3]==6:
                    print("\t############################################################################################################################")
                    print(f"\n\t\t\t\toooooooooooo[[[{team} score =-> {score[1][0]}]]]oooooooooooooooo\n\n")
                    t=False
        else:
            print("wrong input!")#bat ball glat dalega uske liye 
    if score[1][0]>score[2][0]:
        print(f"\n\n\n\t\t\t\t|-> {team} WON <-|")
    elif score[2][0]<score[1][0]:
        print(f"\n\n\n\t\t\t\t|-> {opp} WON <-|")
    elif score[2][0]==0 and score[1][0]==0:
        pass
    elif score[2][0]==score[1][0]:
        print(f"\n\n\n\t\t\t\t|-> {opp} WON <-|")
    else:
        print("~~~~~wrong input~~~~")# teal or head agar glat dale ga uske liye
    

else:
    print("erorr")#team name glat dalega uske liye

    
    
