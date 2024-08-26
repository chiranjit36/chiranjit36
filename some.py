import tkinter as t
from tkinter import messagebox

Box = t.Tk()
Box.title("multliplyer and devider")

label_num1 = t.Label(Box,text="ENTER THE FIRST NUMBER : ")
label_num1.grid(row=0,column=0,padx=10,pady=5)

label2_num2 = t.Label(Box,text="ENTER THE second NUMBER : ")
label2_num2.grid(row=1,column=0,padx=10,pady=5)

entry_num1 = t.Entry(Box)
entry_num1.grid(row=0,column=1,padx=10,pady=5)

entry_num2 = t.Entry(Box)
entry_num2.grid(row=1,column=1,padx=10,pady=5)

button_multliply = t.Button(Box,text="multliply")
button_multliply.grid(row=2,column=0,pady=10)
button_devide = t.Button(Box,text="devider")
button_devide.grid(row=2,column=1,pady=10)

def on_multliply_click(event) :
    num1_text = entry_num1.get()
    num2_text = entry_num2.get()

    if num1_text.replace(',',' ',1).isdigit() and num2_text.replace(',',' ',1).isdigit():
        num1 = float(num1_text)
        num2 = float(num2_text)
        sum_result = num1*num2
        messagebox.showinfo("RESULT",f"The multliply of {num1}and{num2}={sum_result}")

    else:
        messagebox.showerror("Invalid Input,please enter valid numbers")

def on_devide_click(event) :
    num1_text = entry_num1.get()
    num2_text = entry_num2.get()

    if num1_text.replace(',',' ',1).isdigit() and num2_text.replace(',',' ',1).isdigit():
        num1 = float(num1_text)
        num2 = float(num2_text)
        sum_result1 = num1/num2
        messagebox.showinfo("RESULT",f"The devide of {num1}and{num2}={sum_result1}")

    else:
        messagebox.showerror("Invalid Input,please enter valid numbers")        

button_multliply.bind("<Button>",on_multliply_click)
button_devide.bind("<Button>",on_devide_click)
Box.mainloop()
 

