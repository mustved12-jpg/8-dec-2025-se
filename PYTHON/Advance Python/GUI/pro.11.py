
# calculator in text area
from tkinter import *
def my():
    dat=text_area.get(1.0,END)
    dat=dat.split("+")
    l1=[]
    for i in dat:
        name=""
        for j in i:
            if j!="\n":
                name+=j
        l1.append(float(name))
    text_area.delete(1.0,END)
    su=str(sum(l1))
    text_area.insert(END,su)
s=Tk()
total=StringVar()
total.set("")

s.geometry("350x400+900+150")
s.config(background="#d1ff33")
s.title("title")


text_area=Text(s,font=("arial",12),height=1,width=15)
text_area.pack()
Button(s,text="submit",command=my).place(x=170,y=130)

s.mainloop()