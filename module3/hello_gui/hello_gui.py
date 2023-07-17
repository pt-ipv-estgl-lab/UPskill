import tkinter as tk
from tkinter import messagebox


def Click():
    replay = messagebox.askquestion("Quit?", 'Are you sure')
    if replay == 'yes':
        messagebox.showinfo("Info", "I will close the app!")
        my_app.destroy()

my_app = tk.Tk()
my_app.title("My App")
button_1 = tk.Button(my_app, text="Button #1", command='Click')
button_2 = tk.Button(my_app, text="Button #2")
button_3 = tk.Button(my_app, text="Button #3")
button_1.pack(side=tk.RIGHT, fill=tk.Y)
button_2.pack()
button_3.pack()
my_app.mainloop()

