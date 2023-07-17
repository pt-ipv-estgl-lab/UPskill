import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text='Little Label:')
label.pack()

frame = tk.Frame(window, height=30, width=100, bg='#000099')
frame.pack()

button = tk.Button(window, text="Button")
button.pack(fill=tk.X)

switch = tk.IntVar()
switch.set(1)

checkbutton = tk.Checkbutton(window, text='Check Button', variable=switch)
checkbutton.pack()

entry = tk.Entry(window, width=30)
entry.pack()

radiobutton_1 = tk.Radiobutton(window, text='Steak', variable=switch, value=0)
radiobutton_1.pack()
radiobutton_2 = tk.Radiobutton(window, text='Salad', variable=switch, value=1)
radiobutton_2.pack()

window.mainloop()
