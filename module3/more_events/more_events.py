import tkinter as tk
from tkinter import messagebox

def click(event=None):
    if event is None:
        messagebox.showinfo('Click!', 'I love clicks!')
        win.destroy()
    else:
        string = 'x='+ str(event.x) + ', y='+ str(event.y) + \
                ', num='+ str(event.num) + ",type=" + event.type
        messagebox.showinfo('Click!', string)

win = tk.Tk()
label = tk.Label(win, text='Label')
label.bind('<Button-1>', click)
label.pack()

button = tk.Button(win, text='Button', command=click)
button.pack(fill=tk.X)

frame = tk.Frame(win, height=30, width=100, bg='#55BF40')
frame.bind('<Button-2>', click)

frame.pack()

win.mainloop()
