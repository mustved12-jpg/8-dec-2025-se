from tkinter import *

s=Tk()
s.geometry("500x400+600+200")
s.title("box")

teck_data=StringVar()
display_data=StringVar()
display_data.set("")

def myfun():
    global teck_data,display_data
    display_data.set("Hello, "+teck_data.get().title())

s.config(background="#bcaaa4")
tex=Label(s,text="~~welcom~~".upper(),font=("french script mt",20,"bold","underline"),bg="#bcaaa4",fg="#4e342e")
tex.pack()

name=Label(s,text="Enter Your Name :",font=("elephant",15),bg="#a1887f",fg="#6d4c41")
name.place(x=10,y=80)

script=Entry(s,textvariable=teck_data,font=("bell mt",13,"underline"),width=25,bg="#d7ccc8",bd=4)
script.place(x=220,y=80)

button=Button(s,text="submit".title(),font=("arial",15),bg="#5d4037",fg="#212121",activebackground="#90a4ae",activeforeground="#546e7a",command=myfun)
button.place(x=310,y=130)


display=Label(s,textvariable=display_data,font=("elephant",15,"underline"),bg="#bcaaa4",fg="#3e2723")
display.place(x=250,y=180)
s.mainloop()
