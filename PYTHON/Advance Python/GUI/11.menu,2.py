from tkinter import *
from tkinter import filedialog,messagebox
def newfile():
    text_area.delete(1.0,END)# 1.0 matlab suru se pehli line se
def openfile():
    file=filedialog.askopenfilename(filetypes=[("Text Documents","*.txt"),("All files","*.*"),("mustved","*.pdf")])
    if file:                            #                           |txt          or     |ALL    or          |pdf
        f=open(file,'r')                #       ye main hai ye sari txt file jma kar dega isi tra sab kam karte hai
        data=f.read()
        f.close()
        text_area.delete(1.0,END)
        text_area.insert(END,data) 

def savefile():
    file = filedialog.asksaveasfilename(filetypes=[("Text Documents","*.txt"),("All files","*.*")])
    if file:
        data = text_area.get(1.0,END)
        f = open(file,"w")
        f.write(data)
        f.close()
    
def about_us():        # ye tital hai       # ye massage hai
    messagebox.showinfo("notepad 1.0","welcomme to notepade 1.0")
        
s=Tk()
s.geometry("500x400+600+150")
s.config(background="#ff5722")
s.title("Not Book")

text_area=Text(s,font=("elephant",16),width=5,height=1,fg="#3e2723",bg="#ea80fc")
text_area.pack(fill=BOTH,expand=True)# me ne widht or hitght kam diya hu pr isko likhne se ye pure page pe ayega 

All_menu=Menu(s)
# ---------------File
files=Menu(All_menu,tearoff=0)
files.add_command(label="new",accelerator="Ctrl+o",command=newfile)
files.add_command(label="open",accelerator="Ctrl+N",command=openfile)
files.add_command(label="save",command=savefile)
files.add_separator()
files.add_command(label="Exit",command=s.destroy)#s.quit or lambda :s.destroy() ye kilunga to bhi hoga
All_menu.add_cascade(label="File",menu=files)

# --------------About
abouts=Menu(All_menu,tearoff=0)

abouts.add_command(label="about us",command=about_us)
All_menu.add_cascade(label="About",menu=abouts)

# -----------------help
help_menu=Menu(All_menu,tearoff=0)
help_menu.add_command(label="Help")
help_menu.add_separator()
help_menu.add_command(label="version")
All_menu.add_cascade(label="HELP",menu=help_menu)

s.config(menu=All_menu)

s.mainloop()