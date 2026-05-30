import random

def l5050(k,**v):
    global life,d,lst
    life.remove("5️⃣ 0️⃣  —5️⃣ 0️⃣")
    lst.remove(1)
    h=0
    ch=65
    for i1 in range(4):
        if h==2:
            break
        else:
            if d[k][chr(ch)]==d[k]["R"]:
                ch+=1
            else:
                del d[k][chr(ch)]
                h+=1
                ch+=1
                

def freand(k,**v):
    global life,d,lst
    life.remove("🙎")
    lst.remove(2)
    h=0
    ch=65
    for i1 in range(4):
        if h==3:
            break
        else:
            if d[k][chr(ch)]==d[k]["R"]:
                ch+=1
            else:
                del d[k][chr(ch)]
                h+=1
                ch+=1

def poll(k,**v):
    global life,d,lst
    life.remove("poll📊")
    lst.remove(3)
    l1=[]
    r1,r2=25,35
    for i in range(3):
        number=random.randint(r1,r2)
        l1.append(number)
        r1-=10
        r2-=10
    r3=100-sum(l1)
    for i in v.keys():
        if i=="R" or d[k][i]==d[k]["R"]:
            (d[k][i])+=f" ({r3}%)."
            continue
        number=random.choice(l1)
        d[k][i]+=f" ({number}%)."
        l1.remove(number)

d={"Q.1 What is the correct file extension for Python files?":
       {"A":".pt","B":".py","C":".pyt","D":".python","R":".py"},
   "Q.2 Which symbol is used for comments in Python?":
       {"A":"//","B":"#","C":"<!-- -->","D":"**","R":"#"},
   "Q.3 Which data type is mutable in Python?":
       {"A":"Tuple","B":"String","C":"List","D":"Integer","R":"List"},
   "Q.4 Which function is used to take input from the user in Python?":
       {"A":"get()","B":"scan()","C":"read()","D":"input()4","R":"input()"},
   "Q.5 Which keyword is used to define a function in Python?":
        {"A":"function","B":"def","C":"define","D":"fun","R":"def"},
   "Q.6 Which of the following loops are available in Python?":
        {"A":"for loop","B":"while loop","C":"do-while loop","D":"Both A and B","R":"Both A and B"},
   "Q.7 Which of the following is an immutable data type in Python?":
        {"A":"List","B":"Dictionary","C":"Set","D":"Tuple","R":"Tuple"},
   "Q.8 Which bracket is used to create a list in Python?":
        {"A":"{}","B":"()","C":"[]","D":"v","R":"[]"},
   "Q.9 Which of the following is used to store key-value pairs in Python?":
        {"A":"List","B":"Tuple","C":"Set","D":"Dictionary","R":"Dictionary"},
   "Q.10 Which of the following is used to handle exceptions in Python?":
        {"A":"try-except","B":"catch-throw","C":"final-catch","D":"error-handling","R":"try-except"},
   "Q.11 Which operator is used for exponentiation in Python?":
        {"A":"^","B":"**","C":"//","D":"%%","R":"**"},
   "Q.12 Which of the following is true about Python dictionaries?":
        {"A":"Keys can be duplicated","B":"Values must be unique","C":"Keys must be immutable","D":"Dictionaries are ordered in all Python versions","R":"Keys must be immutable"}}
life=["5️⃣ 0️⃣  —5️⃣ 0️⃣","🙎","poll📊","boblue dip ✌️"]
lst=[1,2,3,4]
i=1
one_time=0
U_amount=0
print("----------welcom to KBC game----------")
for k,v in d.items():
    if i==50:
        print(f"""
        you loss the game...
                amount = {0}  😞  """.upper())
        break
    elif i==100:
        print(f"""
        you loss the game...
                amount = {U_amount} 🙁    """.upper())
        break
    if i==1:
        input("\npress enter for quasions......".title())
    else:
        input("\npress enter for next qusions....".title())
    while 1:
        print(f"\n{k}")
        for vk,vv in v.items():
            if vk=="R":
                break# ye break hai R na print karne ke liye 
            print(f"{vk} = {vv}")
        print("------lifeline----")
        for j in range(len(lst)):
            print(f"{lst[j]}.{life[j]}",end="\t\t")
        ans=input("\n\npress your answer :".title()).upper()
        ans2=ans
        if (one_time==1) and (ans=="1" or ans=="2" or ans=="3" or ans=="4"):
            print("one life line at one time.".upper())
            continue# ye hai 1 time pe ek hi life line use hogi uske liye 
        if ans in v.keys() or ans=="1" or ans=="2" or ans=="3" or ans=="4":
            if ans=="R":# ye iske liye hai agar usne r likh to R key me hai to under na jaye iske liye 
                print("\n----------------------------------")
                print("pleas select right option..".title())
                print("----------------------------------\n")
                continue# kers me R hai to agar user ne ABCD ki jgha R press kiya to isse bachne ke liye 
            if ans=="1":
                if "5️⃣ 0️⃣  —5️⃣ 0️⃣" in life:
                    print("""                   
                                USED:<5️⃣ 0️⃣  —5️⃣ 0️⃣>:LIFELINE""")
                    l5050(k,**v)
                    one_time=1
                else:
                    print("you alredy used your <5️⃣ 0️⃣  —5️⃣ 0️⃣> lifeline!!!".title())
                    one_time=0
                continue# agar humne pehle se hi life line use kar liya hioga to isske liye 
            elif ans=="2":
                if "🙎" in life:
                    print("""                   
                                USED:🙎🙎🙎🙎🙎🙎:LIFELINE""")
                    freand(k,**v)
                    one_time=1
                else:
                    print("you alredy used your <🙎> lifeline!!!".title())
                    one_time=0
                continue# agar humne pehle se hi life line use kar liya hioga to isske liye 
            elif ans=="3":
                if "poll📊" in life:
                    print("""                   
                                USED:<POLL📊 >:LIFELINE""")
                    poll(k,**v)
                    one_time=1
                else:
                    print("you alredy used your <poll📊 > lifeline!!!".title())
                    one_time=0
                continue
            elif ans=="4":
                if "boblue dip ✌️" in life:
                    print("""                   
                                USED:<boblue dip ✌️ >:LIFELINE""".upper())
                    while 1:
                        ans1=input("\nenter your first answer :".title()).upper()
                        ans2=input("enter your secound answer :".title()).upper()
                        if ans1=="" or ans2=="":
                            print("\n----------------------------------")
                            print("pleas select right option..".title())
                            print("----------------------------------\n")
                            continue
                        if (ans1 and ans2) in "ABCD":
                            ans=ans1
                            break# agar user ABCD ke kuch bhi dalta hai to 
                        else:
                            print("\n----------------------------------")
                            print("pleas select right option..".title())
                            print("----------------------------------\n")
                            continue # agar ABCD ke alava kuch dalta hai to 
                    life.remove("boblue dip ✌️")
                    lst.remove(4)
                    # one_time=1
                else:
                    print("you alredy used your <boblue dip ✌️> lifeline!!!".title())
                    # one_time=0
                    continue# agar humne use karliya hai to iske liye
            if v[ans]==v["R"] or v[ans2]==v["R"]:
                U_amount+=10000*2
                print(f"""\n
                        |--------------------------------------------|
                          <{v["R"]}> is the right answer......    
                        |--------------------------------------------|
                          current amount = {U_amount}.rs""".upper())
                # break
            else:
                if i>3:
                    i=99
                elif i<=3:
                    i=49
                print("""\n
                        |---------------------------|
                        |  wrong answer......       |
                        |---------------------------|""".upper())
            break# first while break hoga

        else:
            print("\n----------------------------------")
            print("pleas select right option..".title())
            print("----------------------------------\n")
            continue
    one_time=0
    i+=1
if i==len(d.keys())+1:
    print(f"""
    ………………………………………………………………………………………………………………
    ⁞Congratulations You Won The KBC Game. 
    ——————————————————————————————————————————
    ․·․·․·․·․·․·․·․·․·․·․·․·․·․·․·․·․·․·․·․·․·
    ——————————————————————————————————————————
    ⁞ Winnig Amount is >>>> {U_amount}.Rs      
    ⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔""")