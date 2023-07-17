import tkinter as tk
from tkinter import messagebox

def click_1():
    label.config(text=(label.cget('text') + button1.cget('text')))

def click_2():
    label.config(text=(label.cget('text') + button2.cget('text')))

def click_3():
    label.config(text=(label.cget('text') + button3.cget('text')))

def click_4():
    label.config(text=(label.cget('text') + button4.cget('text')))

def click_plus():
    operando = int(label.cget('text'))
    label.config(text='')
    messagebox.showinfo(title='result',message=str(operando+1))

win = tk.Tk()

label = tk.Label(win, text="")
label.grid(row=0, columnspan=4)
button1 = tk.Button(win, text="1", command=click_1)
button1.grid(row=1, column=0)
button2 = tk.Button(win, text="2", command=click_2)
button2.grid(row=1, column=1)
button3 = tk.Button(win, text="3", command=click_3)
button3.grid(row=1, column=2)
button4 = tk.Button(win, text="4", command=click_4)
button4.grid(row=2, column=0)

button_plus = tk.Button(win, text="+", command=click_plus)
button_plus.grid(row=2, column=3)

win.mainloop()