from tkinter import *

s=Tk()
s.title("mustved")
s.geometry("500x300+500+150")
s.config(background="#d7ccc8")
te=Label(s,text="hello all",font=("gigi",20,"underline"),width=10,height=1,bg="blue",fg="red")
te.place(x=100,y=80)

bu=Button(s,text="prees hear",font=("arial",15,"bold"),bd=5,width=10,height=1,activebackground="yellow",activeforeground="white",bg="red",fg="blue")
# activebackground="yellow" is ka matlab hai jub hum click karenge to iska background yellow color ka dikhega 
# activeforeground="white"  is ka matlab hai jub hum click karenge to iska text white color ka dikhega 
bu.place(x=100,y=130)
s.mainloop()



# bd agar hum Button me likehnge to jo humara bottebn hoga uske ajubaju ek bordar type ka bna deta hai
# but agr hum bd ko Label me likhte gai to ye padding ki tra yni height or widht dono ko bdata hai