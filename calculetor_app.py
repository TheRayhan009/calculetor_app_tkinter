import tkinter
from tkinter import *
panel=tkinter.Tk()
def click(event):
    global strvar
    global ans
    input_user=event.widget.cget("text")
    if input_user == "=":
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

input_box=Entry(panel,textvar=strvar,width=26,font=("lucida",24),background="gray")
input_box.grid(row=1,column=1,columnspan=14,ipady=24,pady=10)
#///////////////////////////
num_button_1=Button(panel,text="7",width=15,height=6,background="#717D7E",border="2")
num_button_1.grid(row=2,column=1,sticky="e",padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="8",width=15,height=6,background="#717D7E",border="2")
num_button_1.grid(row=2,column=2)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="9",width=15,height=6,background="#717D7E",border="2")
num_button_1.grid(row=2,column=3,padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="/",width=15,height=6,background="#717D7E",border="2")
num_button_1.grid(row=2,column=4,padx=1,sticky="w")
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="4",width=15,height=6,background="#717D7E",border="2")
num_button_1.grid(row=3,column=1,sticky="e",pady=4,padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="5",width=15,height=6,background="#717D7E",border="2")
num_button_1.grid(row=3,column=2)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="6",width=15,height=6,background="#717D7E",border="2")
num_button_1.grid(row=3,column=3,pady=4,padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="X",width=15,height=6,background="#717D7E",border="2")
num_button_1.grid(row=3,column=4,padx=1,sticky="w")
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="1",width=15,height=6,background="#717D7E",border="2")
num_button_1.grid(row=4,column=1,sticky="e",padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="2",width=15,height=6,background="#717D7E",border="2")
num_button_1.grid(row=4,column=2)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="3",width=15,height=6,background="#717D7E",border="2")
num_button_1.grid(row=4,column=3,padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="-",width=15,height=6,background="#717D7E",border="2")
num_button_1.grid(row=4,column=4,padx=1,sticky="w")
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="0",width=32,height=6,background="#717D7E",border="2")
num_button_1.grid(row=5,column=1,columnspan=2,pady=4,padx=2,sticky="e")
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text=".",width=15,height=6,background="#717D7E",border="2")
num_button_1.grid(row=5,column=3,padx=5)
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_1=Button(panel,text="+",width=15,height=6,background="#717D7E",border="2")
num_button_1.grid(row=5,column=4,padx=1,sticky="w")
num_button_1.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_2=Button(panel,text="=",width=50,height=6,background="#717D7E",border="2")
num_button_2.grid(row=6,column=1,columnspan=10,sticky="w")
num_button_2.bind("<Button-1>",click)
#\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/
num_button_2=Button(panel,text="C",width=15,height=6,background="#717D7E",border="2")
num_button_2.grid(row=6,column=1,columnspan=10,sticky="E")
num_button_2.bind("<Button-1>",click)

# panel.wm_iconbitmap("l.calculator-result")
panel.configure(background="#17202A")
panel.geometry("485x632+875+60")
panel.title("RAYHAN's CALCULATOR")
panel.mainloop()

