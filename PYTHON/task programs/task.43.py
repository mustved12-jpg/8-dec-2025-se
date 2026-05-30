from tkinter import *
from PIL import Image, ImageTk

s = Tk()
s.geometry("800x500")

# Canvas
canvas = Canvas(s, width=800, height=500)
canvas.pack(fill="both", expand=True)

# Image
img = Image.open("PYTHON/Task Programs/IMG_20260504_112135.jpg").resize((800, 500))

bg = ImageTk.PhotoImage(img)

# Background image show
canvas.create_image(0, 0, image=bg, anchor="nw")

# Text directly on image
canvas.create_text(600, 200,text="WELCOME",font=("Arial", 35, "bold"),fill="white",)


s.mainloop()