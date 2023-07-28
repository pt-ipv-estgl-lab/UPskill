import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox

root = tk.Tk()
root.title("Media Lib App")

window_width = 640
window_height = 480

# get the screen dimension
screen_width = root.winfo_screenwidth()
#print('screen width:', screen_width)
screen_height = root.winfo_screenheight()
# print('screen height:', screen_height)

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# root.attributes('-alpha', 0.8)~

def friend_window():
    # Create secondary (or popup) window.
    global center_x
    global center_y

    window = tk.Toplevel()
    window.title('Friend')
    window.geometry(f'300x200+{center_x}+{center_y}')
    # configure the grid
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)
    # nickname
    nickname_label = ttk.Label(window, text="Nickname:")
    nickname_label.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

    nickname_entry = ttk.Entry(window)
    nickname_entry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

    # name
    name_label = ttk.Label(window, text="Name:")
    name_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

    name_entry = ttk.Entry(window)
    name_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

    # email
    email_label = ttk.Label(window, text="Email:")
    email_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

    email_entry = ttk.Entry(window)
    email_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

    # save button
    save_button = ttk.Button(window, text="Save")
    save_button.grid(column=0, row=3, sticky=tk.SW, padx=5, pady=5)

    # cancel button
    cancel_button = ttk.Button(window, text="Cancel", command=window.destroy)
    cancel_button.grid(column=1, row=3, sticky=tk.SE, padx=5, pady=5)
    window.focus()
    window.grab_set() # Modal.


def menu_about():
    messagebox.showinfo('About', 'Demo on Upskill course')

# create a menubar
menubar = Menu(root)

# create a menu
management_menu = Menu(menubar, tearoff=0)

# add menu items to the management menu
management_menu.add_command(label='Products')

# add the submenu to friends
friends_submenu = Menu(management_menu, tearoff=False)
friends_submenu.add_command(label='Create', command=friend_window)
friends_submenu.add_command(label='Retrieve')
friends_submenu.add_command(label='Update')
friends_submenu.add_command(label='Delete')
management_menu.add_cascade(label='Friends', menu=friends_submenu)

# management_menu.add_separator()

# add the Management menu to the menubar
menubar.add_cascade(
    label="Managment",
    menu=management_menu
)

loan_menu = Menu(menubar, tearoff=0)
loan_menu.add_command(label='New')
menubar.add_cascade(label='Loans', menu=loan_menu)

list_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='List', menu=list_menu)

# add Exit menu item
menubar.add_command(
    label='Exit',
    command=root.destroy
)

menubar.add_command(label='About',
                    command=menu_about)

root.config(menu=menubar)
root.mainloop()