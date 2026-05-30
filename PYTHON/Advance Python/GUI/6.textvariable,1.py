from io import text_encoding
from tkinter import *
def my():
    dat=text_area.get(1.0,END)
    total.set(dat)
    print(dat)
s=Tk()
total=StringVar()
total.set("")
s.geometry("500x400+600+150")
s.config(background="#d1ff33")
s.title("title")


text_area=Text(s,width=10,height=2,font=("airal",12))
text_area.pack()

Button(s,text="submit",font=("elephant",26,"underline"),bg="blue",fg="red",activebackground="red",activeforeground="blue",command=my).pack()

Label(s,textvariable=total,font=("arial",26,"underline"),height=1,bg="white",fg="red").place(x=150,y=150)

s.mainloop()
