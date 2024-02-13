import tkinter
from tkinter import *
import os
import math
panel=tkinter.Tk()
def click(event):
    global strvar
    global ans
    input_user=event.widget.cget("text")
    if input_user == "√":
        strvar.set(math.sqrt(int(strvar.get())))
        ans=list(strvar.get())
        ans.pop()
        ans=int(ans)
        strvar.set(ans)
        input_box.update()
    if input_user == "=":
        if "^" in strvar.get():
            X_chak = strvar.get().replace("^", "**")
            ans=eval(X_chak)
            strvar.set(ans)
        elif "w" in strvar.get():
            X_chak = strvar.get().replace("w", "mg")
            strvar.set(X_chak)
        elif "%" in strvar.get():
            # X_chak = strvar.get().replace("^", "**")
            ans=eval(strvar.get())
            strvar.set(ans)
        elif "G" in strvar.get():
            X_chak = strvar.get().replace("G", "6.67×10^−11")
            ans=X_chak
            strvar.set(ans)
        elif "h" in strvar.get():
            X_chak = strvar.get().replace("h", "6.634×10^−34")
            ans=X_chak
            strvar.set(ans)
        elif "g" in strvar.get():
            X_chak = strvar.get().replace("g", "9.8")
            ans=X_chak
            strvar.set(ans)
        else:
            X_chak = strvar.get().replace("X", "*")
            ans=eval(X_chak)
            strvar.set(ans)
        input_box.update()
    elif input_user =="C":
        strvar.set(" ")
        input_box.update()
    else:
        strvar.set(strvar.get()+input_user)
        input_box.update()



strvar=StringVar()
strvar.set("")

#//////////////////////////////////////////////////////////////////////////////////

input_box=Entry(panel,textvar=strvar,width=33,font=("lucida",24),background="gray")
input_box.grid(row=1,column=1,columnspan=14,ipady=24,pady=10)
#///////////////////////////
num_button_1=Button(panel,text="7",width=15,height=6,background="#585858",border="2",fg="white")
num_button_1.grid(row=2,column=1,sticky="e",padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="8",width=15,height=6,background="#585858",border="2",fg="white")
num_button_1.grid(row=2,column=2)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="9",width=15,height=6,background="#585858",border="2",fg="white")
num_button_1.grid(row=2,column=3,padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="/",width=15,height=6,background="#B45F04",border="2",fg="white")
num_button_1.grid(row=2,column=4,padx=1,sticky="w")
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="G",width=15,height=6,background="red",border="2",fg="white")
num_button_1.grid(row=2,column=5,padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="4",width=15,height=6,background="#585858",border="2",fg="white")
num_button_1.grid(row=3,column=1,sticky="e",pady=4,padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="5",width=15,height=6,background="#585858",border="2",fg="white")
num_button_1.grid(row=3,column=2)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="6",width=15,height=6,background="#585858",border="2",fg="white")
num_button_1.grid(row=3,column=3,pady=4,padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="X",width=15,height=6,background="#B45F04",border="2",fg="white")
num_button_1.grid(row=3,column=4,padx=1,sticky="w")
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="g",width=15,height=6,background="red",border="2",fg="white")
num_button_1.grid(row=3,column=5,padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="1",width=15,height=6,background="#585858",border="2",fg="white")
num_button_1.grid(row=4,column=1,sticky="e",padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="2",width=15,height=6,background="#585858",border="2",fg="white")
num_button_1.grid(row=4,column=2)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="3",width=15,height=6,background="#585858",border="2",fg="white")
num_button_1.grid(row=4,column=3,padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="-",width=15,height=6,background="#B45F04",border="2",fg="white")
num_button_1.grid(row=4,column=4,padx=1,sticky="w")
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="h",width=15,height=6,background="red",border="2",fg="white")
num_button_1.grid(row=4,column=5,padx=1)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="0",width=32,height=6,background="#585858",border="2",fg="white")
num_button_1.grid(row=5,column=1,columnspan=2,pady=4,padx=2,sticky="e")
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text=".",width=15,height=6,background="#585858",border="2",fg="white")
num_button_1.grid(row=5,column=3,padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="+",width=15,height=6,background="#B45F04",border="2",fg="white")
num_button_1.grid(row=5,column=4,padx=1,sticky="w")
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="w",width=15,height=6,background="red",border="2",fg="white")
num_button_1.grid(row=5,column=5,padx=1)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_2=Button(panel,text="=",width=15,height=6,background="#B45F04",border="2",fg="white")
num_button_2.grid(row=6,column=1,padx=2)
num_button_2.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_2=Button(panel,text="^",width=15,height=6,background="#B45F04",border="2",fg="white")
num_button_2.grid(row=6,column=2,padx=2)
num_button_2.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_2=Button(panel,text="√",width=15,height=6,background="#B45F04",border="2",fg="white")
num_button_2.grid(row=6,column=3)
num_button_2.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_2=Button(panel,text="%",width=15,height=6,background="#B45F04",border="2",fg="white")
num_button_2.grid(row=6,column=4)
num_button_2.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_2=Button(panel,text="C",width=15,height=6,background="#424242",border="2",fg="white")
num_button_2.grid(row=6,column=5)
num_button_2.bind("<Button-1>",click)

# image=PhotoImage(file="D:\\rayhan-drive\\Tkinter_project\\calculator-result.jpg")
# panel.iconphoto(False,image)

panel.iconbitmap("Tkinter_project\logo.ico")

panel.configure(background="#17202A")
panel.geometry("610x630+750+60")
panel.title("RAYHAN's CALCULATOR")
panel.mainloop()

