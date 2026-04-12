import random
l1=["CSK","MI","GT","RR","RCB","KKR"]
h_t=["TEAL","HEAD"]#    USER     OPP    
#                     R W O B   R W O B   /R=run,W=wicket,O=over,B=ball 
score=["SCORE BOARD",[0,0,0,0],[0,0,0,0]]
balls=[0,1,2,3,4,6,"wide ball","no ball","wicket"]
for i in range(len(l1)):
    if i==0:
        print("\n\n\n\t  -----------------:IPL 2026 :-------------------\n\n")
    print(f"\t  ({l1[i]})",end="")
print("\n")
t=True
while t:
    print("\n\n____________________________________")
    print("|                                  |")
    team=input("\tenter your team name :".upper()).upper()
    print("                              ----")
    for i in l1:
        if team==i:
            flage=1
            break
        else:
            flage=0
    u,p=0,0# ye check karne ke liye ki (user & opp) ki tem me se aya hai ki nhi u line 47 and p line 118 pe hai
    if flage==1:
        l1.remove(team)
        opp=random.choice(l1)
        print(f"\toppnet team : {opp}".upper())
        print("|__________________________________|\nTOSS TIME:\n")
        print("\t H/T\n")
        actual=random.choice(h_t)
        user=input("enter your toss choice:".upper()).upper()
        if ((user=="H" and actual=="HEAD") or (user=="T" and  actual=="TEAL")) or user==actual:
            print(f"~~~~~~~~~~~~~~~~':{team} won the toss:'~~~~~~~~~~~~~~~~~~~~~~\n")
            bb_ch=input("enter your choice (bat/bALl) :".upper()).upper()                
            if bb_ch=="BAT" or bb_ch=="BALL":
                if bb_ch=="BAT":
                    ok=1# agar user bat(ok=1) choice karta hai to pehle ye vala chalega fir isme last me ok=2 countinue hai jisse ye
                else:#  dobara bat(ok=1) me nhi aye ga
                    ok=2# sem agar user ball(ok=2 ) choice karega 
                while t:
                    if score[1][1]==2 and score[2][1]==2:# agar dono wicket se out honge to yha se breck hoga
                        t=False
                    if ok==1:
                        u=1# ye btane ke liye ki code yha se ja chuka hai
                        print(f"\n\t\t<<<<<<<<<<<<({team}: bating.......)>>>>>>>>>>>>>>>>>\n")
                        print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
                        print("\n\t\t*********************************************\n")
                        noball=0
                        while t:
                            balling=random.choice(balls)
                            input("\n\t~.^.~.^.~.^.~.^.~.^.~.^.~:press enter:<o_o>")
                            if score[2][3]==6:
                                score[2][2]+=1
                                score[2][3]=0

                            if balling==balls[7]:#noball
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
                                if score[1][1]>=2:
                                    print("\t############################################################################################################################")
                                    print(f"\n\t\t\t\toooooooooooo[[[{team} score =-> {score[1][0]}]]]oooooooooooooooo\n\n")
                                    print("\t############################################################################################################################\n\n")
                                    ok=3# ye agar 2 bar out ho gya uske liye hai isse vo dosri time ke pas jaye ga 
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
                                print("\t############################################################################################################################\n\n")
                                break# inner loo break hone ke bad ye else me jayega 
                            if p==1:
                                if score[2][0]<score[1][0]:
                                    t=False
                        if (score[1][0]>0 or score[1][1]>0) and (score[2][0]>0 or score[2][1]>0):
                            t=False
                        elif ok==3:# ye agar 2 bar out ho gya uske liye hai
                            ok=2
                            rune=1
                            continue
                        else:
                            ok=2
                            continue
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<opp bating>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    elif ok==2:
                        p=1# ye btane ke liye li code yha se ho ke ja chuka hai
                        print(f"<><><><><><><><><>:{opp} bating...:<><><><><><><><>".upper())
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
                                if score[2][1]>=2:
                                    print("\t############################################################################################################################")
                                    print(f"\n\t\t\t\toooooooooooo[[[{opp} score =-> {score[2][0]}]]]oooooooooooooooo\n\n")
                                    print("\t############################################################################################################################\n\n")
                                    ok=3# ye agar 2 bar out ho gya uske liye hai isse vo dosri team ke pas jaye ga 
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
                                print("\t############################################################################################################################\n\n")
                                break#inner loop break hone ke bad ye else me jayega 
                            if u==1:
                                if score[2][0]>score[1][0]:
                                    t=False
                        if (score[1][0]>0 or score[1][1]>0) and (score[2][0]>0 or score[2][1]>0):
                            t=False
                        elif ok==3:# ye agar 2 bar out ho gya uske liye hai isse vo dosri team ke pas jaye ga 
                            ok=1
                            continue
                        else:
                            ok=1
                            continue
            else:
                print("\n~!!~ wrong input press only : (bat/ball)".upper())
                l1.append(team)
                continue
#=========================================================bating end
            
                    
        elif ((user=="T" and actual=="HEAD") or (user=="H" and  actual=="TEAL")) or ((user=="HEAD" and actual=="TEAL") or(user=="TEAL" and actual=="HEAD")):
            bb=["BALL","BAT"]
            bb_ran=random.choice(bb)
            print(f"~~~~~~~~~~~~~~~~':{opp} won the toss:'~~~~~~~~~~~~~~~~~~~~~~\n")
            if bb_ran=="BAT" or bb_ran=="BALL":
                if bb_ran=="BAT":
                    ok=1# agar user bat(ok=1) choice karta hai to pehle ye vala chalega fir isme last me ok=2 countinue hai jisse ye
                else:#  dobara bat(ok=1) me nhi aye ga
                    ok=2# sem agar user ball(ok=2 ) choice karega 
                while t:
                    if score[1][1]==2 and score[2][1]==2:# agar dono wicket se out honge to yha se breck hoga
                        t=False
                    if ok==1:
                        u=1# ye btane ke liye ki code yha se ja chuka hai
                        print(f"\n\t\t<<<<<<<<<<<<({team}: bating.......)>>>>>>>>>>>>>>>>>\n")
                        print(f"\t\t{score[0]} : {team} : {score[1][0]}/{score[1][1]}  ({score[2][2]}.{score[2][3]}) overs".upper())
                        print("\n\t\t*********************************************\n")
                        noball=0
                        while t:
                            balling=random.choice(balls)
                            input("\n\t~.^.~.^.~.^.~.^.~.^.~.^.~:press enter:<o_o>")
                            if score[2][3]==6:
                                score[2][2]+=1
                                score[2][3]=0

                            if balling==balls[7]:#noball
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
                                if score[1][1]>=2:
                                    print("\t############################################################################################################################")
                                    print(f"\n\t\t\t\toooooooooooo[[[{team} score =-> {score[1][0]}]]]oooooooooooooooo\n\n")
                                    print("\t############################################################################################################################\n\n")
                                    ok=3# ye agar 2 bar out ho gya uske liye hai isse vo dosri time ke pas jaye ga 
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
                                print("\t############################################################################################################################\n\n")
                                break# inner loo break hone ke bad ye else me jayega 
                            if p==1:
                                if score[2][0]<score[1][0]:
                                    t=False
                        if (score[1][0]>0 or score[1][1]>0) and (score[2][0]>0 or score[2][1]>0):
                            t=False
                        elif ok==3:# ye agar 2 bar out ho gya uske liye hai
                            ok=2
                            rune=1
                            continue
                        else:
                            ok=2
                            continue
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<opp bating>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    elif ok==2:
                        p=1# ye btane ke liye li code yha se ho ke ja chuka hai
                        print(f"<><><><><><><><><>:{opp} bating...:<><><><><><><><>".upper())
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
                                if score[2][1]>=2:
                                    print("\t############################################################################################################################")
                                    print(f"\n\t\t\t\toooooooooooo[[[{opp} score =-> {score[2][0]}]]]oooooooooooooooo\n\n")
                                    print("\t############################################################################################################################\n\n")
                                    ok=3# ye agar 2 bar out ho gya uske liye hai isse vo dosri team ke pas jaye ga 
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
                                print("\t############################################################################################################################\n\n")
                                break#inner loop break hone ke bad ye else me jayega 
                            if u==1:
                                if score[2][0]>score[1][0]:
                                    t=False
                        if (score[1][0]>0 or score[1][1]>0) and (score[2][0]>0 or score[2][1]>0):
                            t=False
                        elif ok==3:# ye agar 2 bar out ho gya uske liye hai isse vo dosri team ke pas jaye ga 
                            ok=1
                            continue
                        else:
                            ok=1
                            continue
            else:
                print("\n~!!~ wrong input press only : (bat/ball)".upper())
                l1.append(team)
                continue
        else:
            print("\n\n!!! wonrg input enter head(h) or teal(t) !!!".upper())
            l1.append(team)
            continue
    else:
        print("\n\n!!!wrong team name!!!".upper())
        continue
print("\n\n_______________________________________________________________________________________________________")
print("_______________________________________________________________________________________________________")
print("_______________________________________________________________________________________________________")
print("_______________________________________________________________________________________________________\n\n")
if score[1][0]>score[2][0]:
    print(f"\t\t\t\t\t>>>THE WINNER OF 2026 IS {team}<<<")
elif score[1][0]<score[2][0]:
    print(f"\t\t\t\t\t>>>THE WINNER OF 2026 IS {opp}<<<")
else:
    print(f"\t\t\t\t\t>>>|||||||||D R O W||||||||||<<<")

print("\n\n_______________________________________________________________________________________________________")
print("_______________________________________________________________________________________________________")
print("_______________________________________________________________________________________________________")
print("_______________________________________________________________________________________________________\n\n")