from random import random
import random

menu="""\n
               -----------IPL 2026:----------
              |                              |
              |  CSK  MI  GT  RR  RCB  KKR   |
              |                              |
               ------------------------------ 
\n"""

print(menu)

team=input("enter your team name :".upper()).upper()

l1=["CSK","MI","GT","RR","RCB","KKR"]

for i in l1:
    if team==i:
        w=1
        l1.remove(i)
    else:
        w=0
if w==1:
    print("wrong team")
    opp=random.choice(l1)
    print(f"oppnet team : {opp}".upper())

    

    status=True

    t=["HEAD","TEAL"]
    bb=['BAT','BOL']
    toss=random.choice(t)
    bb_ren=random.choice(bb)
    toss_ch=input("enter your toss choice :".upper()).upper()

    if toss_ch==toss or ((toss_ch=="H" and toss=="HEAD")or(toss_ch=="T" and toss=="TEAL")):
        print("you won the toss chose <<bat>> or <<bol>>")
        play=input("enter your choice (bat/bol) :".upper()).upper()

    elif ((toss_ch=="HEAD" and toss=="TEAL")or(toss_ch=="TEAL" and toss=="HEAD")) or ((toss_ch=="H" and toss=="TEAL")or(toss_ch=="T" and toss=="HEAD")):
        print("you lose")
        print("oponet choice :",bb_ren)
    else:
        print("rong input!!!")
        
        pass
    while status:

        break
else:
    print("wrong team!!!")