from tkinter import*
import re
All=""
p=""
def enter(num):
    global okok,All
    if type(num)==int:# agar paramiter int hoga to isme jayega jab me Ce dbaun ga to num int me ayega 
        All=""
    else:
        if All=="":#agar All pehel khali hoga to hmara number isme ayega mene pehel 5 diya to ye yha ayega
            if num in "x+%÷-":#agar pehle opreter dalega to nhi jayega
                pass
            else: 
                All+=num
        elif num!=All[-1]:# fir sare number isme ayege jo iske pehle vale number se alag 
            # honge fir mene 6 diya to yha aye ga agar me fir 5 dunga to yha nhi else me kayega  
            All+=num
        else:
            if num in "x+÷-%":# agar jo hum enter karenge vo inme se honge to kuch bhi nhi add hoga 
                pass#ye is liye hai ki agar mene + dala hu or fir + dalunga to nhi hoga 
            else:#or isme agar mne 8 dala fir 8 dalunga to add hoga 
                All+=num# agar unme se nhi honge to add hoga 
    okok.set(All)
def back():
    global All
    All=All[:len(All)-1]
    okok.set(All)
def total():
    global All,p
    if All[0]=="-":# agar -32+321 mines se suru hota hoga to isme jayega 
        All="(negetiv)not allowed!"# isko mene is liye alag rakha hu q ki 5-10 karne ke bad -5 aya fir mene +10 ye ayega
        okok.set(All)
        All=""
        return
    data=re.split(r"[x+%÷-]",All)
    Sum=float(data[0])
    for i in All: 
        if i in "x+%÷-":
            p+=i
            # 231+246-323x5
            # 231,246,323,5
            # +-x
    for i in range(1,len(p)+1):
        if p[i-1]=="x":
            Sum*=float(data[i])
        elif p[i-1]=="+":
            Sum+=float(data[i])
        elif p[i-1]=="-":
            Sum-=float(data[i])
        elif p[i-1]=="÷":
            Sum/=float(data[i])
        elif p[i-1]=="%":
            Sum=round(((Sum*float(data[i]))/100),2)
    All=str(Sum)
    p=""
    okok.set(Sum)
s=Tk()
okok=StringVar()
s.title("ok")
s.geometry("300x400+900+150")
s.config(background="#fce4ec")

Button(s,text="+",font=("arial",15,"bold"),height=3,width=3,bg="#d81b60",fg="black",bd=5,command=lambda:enter("+")).place(x=230,y=250)
Button(s,text="-",font=("arial",15,"bold"),width=3,height=1,bg="#d81b60",fg="black",bd=5,command=lambda:enter("-")).place(x=230,y=200)
Button(s,text="x",font=("arial",15,"bold"),width=3,height=1,bg="#d81b60",fg="black",bd=5,command=lambda:enter("x")).place(x=230,y=150)
Button(s,text="÷",font=("arial",15,"bold"),width=3,height=1,bg="#d81b60",fg="black",bd=5,command=lambda:enter("÷")).place(x=230,y=100)


Button(s,text="0",font=("arial",15,"bold"),width=4,height=1,bg="#ce93d8",fg="black",bd=5,command=lambda:enter("0")).place(x=20,y=300)
Button(s,text=".",font=("arial",15,"bold"),width=4,height=1,bg="#d81b60",fg="black",bd=5,command=lambda:enter(".")).place(x=90,y=300)
Button(s,text="=",font=("arial",15,"bold"),width=4,height=1,bg="#d81b60",fg="black",bd=5,command=total).place(x=160,y=300)


Button(s,text="1",font=("arial",15,"bold"),width=4,height=1,bg="#ce93d8",fg="black",bd=5,command=lambda:enter("1")).place(x=20,y=250)
Button(s,text="2",font=("arial",15,"bold"),width=4,height=1,bg="#ce93d8",fg="black",bd=5,command=lambda:enter("2")).place(x=90,y=250)
Button(s,text="3",font=("arial",15,"bold"),width=4,height=1,bg="#ce93d8",fg="black",bd=5,command=lambda:enter("3")).place(x=160,y=250)

Button(s,text="4",font=("arial",15,"bold"),width=4,height=1,bg="#ce93d8",fg="black",bd=5,command=lambda:enter("4")).place(x=20,y=200)
Button(s,text="5",font=("arial",15,"bold"),width=4,height=1,bg="#ce93d8",fg="black",bd=5,command=lambda:enter("5")).place(x=90,y=200)
Button(s,text="6",font=("arial",15,"bold"),width=4,height=1,bg="#ce93d8",fg="black",bd=5,command=lambda:enter("6")).place(x=160,y=200)

Button(s,text="7",font=("arial",15,"bold"),width=4,height=1,bg="#ce93d8",fg="black",bd=5,command=lambda:enter("7")).place(x=20,y=150)
Button(s,text="8",font=("arial",15,"bold"),width=4,height=1,bg="#ce93d8",fg="black",bd=5,command=lambda:enter("8")).place(x=90,y=150)
Button(s,text="9",font=("arial",15,"bold"),width=4,height=1,bg="#ce93d8",fg="black",bd=5,command=lambda:enter("9")).place(x=160,y=150)

Button(s,text="⮜",font=("arial",15,"bold"),width=4,height=1,bg="#d81b60",fg="black",bd=5,command=back).place(x=20,y=100)
Button(s,text="CE",font=("arial",15,"bold"),width=4,height=1,bg="#d81b60",fg="black",bd=5,command=lambda:enter(0)).place(x=90,y=100)
Button(s,text="%",font=("arial",15,"bold"),width=4,height=1,bg="#d81b60",fg="black",bd=5,command=lambda:enter("%")).place(x=160,y=100)

text=Label(s,textvariable=okok,font=("arial",15,"bold"),bg="#a7ffeb",fg="#ad1457",width=17,height=1,bd=5,relief="solid",anchor="e")
text.place(x=50,y=30)
s.mainloop()
