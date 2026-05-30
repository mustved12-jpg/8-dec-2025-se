from tkinter import *
from PIL import Image, ImageTk
# pip install pillow

s=Tk()
s.geometry("500x400")

img=Image.open("PYTHON/Task Programs/IMG_20260504_112135.jpg").resize((500, 400))
# img = img.resize((500, 400))
bg_image = ImageTk.PhotoImage(img)
bg_label = Label(s, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


Button(s,text="mustved",font=("arial",20,"bold")).pack()
main=Menu(s)
f_menu=Menu(main,tearoff=0)
f_menu.add_command(label="new")
main.add_cascade(label="file",menu=f_menu)
s.config(menu=main)

s.mainloop()