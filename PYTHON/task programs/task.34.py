import random
from tkinter import *

s=Tk()
s.title("rock-paper-scissor game.".title())
s.geometry("700x500")
s.config(background="#69f0ae")
h=Label(s,text="welcom to rock~paper~scissor game".upper(),font=("arial",22,"bold","italic","underline"),bg="#69f0ae",fg="#004d40")
h.pack()
def myfun(p):
    pass


b=Button(s,text="Rock",font=("arial",20,"bold"),bg="#388e3c",fg='#c8e6c9',command=lambda:myfun("Rock"))
b.place(x=150,y=80)
b=Button(s,text="Paper",font=("arial",20,"bold"),bg="#388e3c",fg='#c8e6c9',command=lambda:myfun("Paper"))
b.place(x=300,y=80)
b=Button(s,text="Scissor",font=("arial",20,"bold"),bg="#388e3c",fg='#c8e6c9',command=lambda:myfun("Scissor"))
b.place(x=450,y=80)

user=Label(s,text="User",font=("arial",20,"bold","underline"),bg="#69f0ae",fg="#424242")
user.place(x=1,y=200)
user=Label(s,text="~>> ",font=("arial",18,"bold"),bg="#69f0ae",fg="#424242")
user.place(x=80,y=200)

computer=Label(s,text="Coumputer",font=("arial",20,"bold","underline"),bg="#69f0ae",fg="#424242")
computer.place(x=1,y=250)
computer=Label(s,text="~>> ",font=("arial",18,"bold"),bg="#69f0ae",fg="#424242")
computer.place(x=170,y=250)



s.mainloop()