from tkinter import *
s=Tk()
s.geometry("600x500")
s.title("mustved")
Label(s,text="hello\nim mustved".title(),font=("arial",26,"bold"),bg="pink",fg=("red")).pack()
Label(s,text="im the booss".upper(),font=("arial",20,"italic","bold"),bg="yellow",fg="green").pack()
Label(s,text="im the booss".upper(),font=("arial",20,"italic","bold"),bd=50,bg="green",fg="blue").pack()
Label(s,text="im the booss".upper(),font=("arial",20,"italic","bold"),width=50,height=1,bg="red",fg="pink").pack()
s.mainloop()