from tkinter import *

s=Tk()
s.geometry("500x400+600+150")
s.config(background="#ea80fc")
s.title("Not Book")

All_menu=Menu(s)
# ---------------File
files=Menu(All_menu,tearoff=0)
files.add_command(label="new")
files.add_command(label="open")
files.add_command(label="save")
files.add_separator()
files.add_command(label="Exit")
All_menu.add_cascade(label="File",menu=files)

# --------------About
abouts=Menu(All_menu,tearoff=0)

abouts.add_command(label="about us")
All_menu.add_cascade(label="About",menu=abouts)

# -----------------help
help_menu=Menu(All_menu,tearoff=0)
help_menu.add_command(label="Help")
help_menu.add_separator()
help_menu.add_command(label="version")
All_menu.add_cascade(label="HELP",menu=help_menu)

s.config(menu=All_menu)

s.mainloop()