import random
from tkinter import *
s=Tk()
user_name_tk=StringVar()
user_score_tk=IntVar()
computer_name_tk=StringVar()
computer_score_tk=IntVar()

winer=StringVar()

just="mustved"

u,c=0,0
user_name_tk.set("panding")
computer_name_tk.set("panding")
user_score_tk.set(0)
computer_score_tk.set(0)

def myfun(name):
    global u,c
    user_name_tk.set(name)
    l1=["Rock","Papper","Scissor"]
    co_ch=random.choice(l1)
    computer_name_tk.set(co_ch)

    if (name=="Rock" and co_ch=="Papper") or (name=="Papper" and co_ch=="Scissor") or (name=="Scissor" and co_ch=="Rock"):
        c+=1
        winer.set("Computer Winner")
    elif (co_ch=="Rock" and name=="Papper") or (co_ch=="Papper" and name=="Scissor") or (co_ch=="Scissor" and name=="Rock"):
        u+=1
        winer.set("User Winner")
    else:
        winer.set("-----Drow----")
    user_score_tk.set(u)
    computer_score_tk.set(c)
    Label(s,textvariable=winer,font=("airal",20,"bold","underline"),width=20,bg="blue",fg="yellow").place(x=100,y=350)
    


s.title("Game")                     #               y|  
#                                                   200.....   
                                #                    |     :
s.geometry("500x400+750+200")  #                     |____750___x

s.config(background="#bcaaa4")

tt=Label(s,text="welcom to the game.".title(),font=("arial",20,'bold'),height=1,width=80,bg="red",fg="#424242")
tt.pack()

rock=Button(s,text="Rock",font=("bauhaus 93",15,"bold"),bd=15,bg="green",fg="red",activebackground="red",activeforeground="blue",command=lambda:myfun("Rock"))
rock.place(x=50,y=100)

papper=Button(s,text="Papper",font=("bauhaus 93",15,"bold"),bd=15,bg="green",fg="red",activebackground="red",activeforeground="blue",command=lambda:myfun("Papper"))
papper.place(x=200,y=100)

scissor=Button(s,text="Scissor",font=("bauhaus 93",15,"bold"),bd=15,bg="green",fg="red",activebackground="red",activeforeground="blue",command=lambda:myfun("Scissor"))
scissor.place(x=370,y=100)
# ---------------------user

user=Label(s,text="User --->",font=("gigi",16,"bold"),bg="#bcaaa4",fg="blue")
user.place(x=10,y=200)

user_ch=Label(s,textvariable=user_name_tk,font=("ink free",15,"bold"),bg="green",fg="red")
user_ch.place(x=200,y=200)

user_sco=Label(s,textvariable=user_score_tk,font=("ink free",15,"bold"),bg="green",fg="red")
user_sco.place(x=350,y=200)


# ---------------computer

computer=Label(s,text="Computer --->",font=("gigi",16,"bold"),bg="#bcaaa4",fg="blue")
computer.place(x=10,y=250)

computer_ch=Label(s,textvariable=computer_name_tk,font=("ink free",15,"bold"),bg="green",fg="red")
computer_ch.place(x=200,y=250)

computer_sco=Label(s,textvariable=computer_score_tk,font=("ink free",15,"bold"),bg="green",fg="red")
computer_sco.place(x=350,y=250)

s.mainloop()