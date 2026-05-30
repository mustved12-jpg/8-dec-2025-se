from tkinter import *
def ok():
    data=text_area.get(1.0,END)
    print(data)

    
s=Tk()
s.geometry("400x300+700+150")
s.config(background="#ea80fc")#pink color


Button(s,text="get",command=ok).pack()


text_area=Text(s,font=("french script mt",25,"bold"),bg="yellow",fg="red")
text_area.pack(fill=BOTH,expand=True)#ye pure kinter ke brabar ka ho jaye ga isme hum text likhenge jo isme save hoga 


s.mainloop()