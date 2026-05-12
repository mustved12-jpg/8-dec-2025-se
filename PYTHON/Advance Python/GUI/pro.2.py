from tkinter import Pack
from tkinter import Label
from tkinter import *
s=Tk()
s.geometry('400x400')
s.title("mustved")

t=Label(s,text="welcomt to my GUI app..").pack()
t=Label(s,text="welcomt to my GUI app..".upper()).pack()
t=Label(s,text="welcomt to my GUI app..".title())
t.pack()


s.mainloop()