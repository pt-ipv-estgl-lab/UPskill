import tkinter as tk
from tkinter import messagebox

def click():
    messagebox.showinfo('Text', entry.get())

win = tk.Tk()

label = tk.Label(text='Name:')
label.pack()

entry = tk.Entry()
entry.pack()

button = tk.Button(text='Info', command=click)
button.pack()

win.mainloop()