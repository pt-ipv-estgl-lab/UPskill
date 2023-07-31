import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox

class MainWindow(tk.Tk):
    def __init__(self, window_width = 640, window_height = 480, *args, **kargs):
        super().__init__(*args, **kargs)
        self.title("Media Lib App")

        # find the center point
        __screenwith = self.winfo_screenwidth()
        __screenheight = self.winfo_screenheight()

        __center_x = int(__screenwith/2 - window_width / 2)
        __center_y = int(__screenheight/2 - window_height / 2)

        # set the position of the window to the center of the screen
        print(f'{window_width}x{window_height}+{__center_x}+{__center_y}')
        self.geometry(f'{window_width}x{window_height}+{__center_x}+{__center_y}') # geometry configuration
        # self.resizable(False,False)
        self.iconbitmap('./assets/PV_logotipo_pequeno.ico') # change app icon

        # self.attributes('-alpha', 0.9) # transparency
        # create a menubar
        __menubar = Menu(self)

        # create a menu
        __management_menu = Menu(__menubar, tearoff=0)

        # add menu items to the management menu
        __management_menu.add_command(label='Products')
        __management_menu.add_command(label='Friends')

        # # management_menu.add_separator()

        # add the Management menu to the menubar
        __menubar.add_cascade(
            label="Managment",
            menu=__management_menu
        )

        __loan_menu = Menu(__menubar, tearoff=0)
        __loan_menu.add_command(label='New')
        __menubar.add_cascade(label='Loans', menu=__loan_menu)

        __report_menu = Menu(__menubar, tearoff=0)
        __menubar.add_cascade(label='Repors', menu=__report_menu)

        # add Exit menu item
        __menubar.add_command(
            label='Exit',
            command=self.destroy
        )
        self.config(menu=__menubar)

    # def friend_window():
    #     # Create secondary (or popup) window.
    #     global center_x
    #     global center_y

    #     window = tk.Toplevel()
    #     window.title('Friend')
    #     window.geometry(f'300x200+{center_x}+{center_y}')
    #     # configure the grid
    #     window.columnconfigure(0, weight=1)
    #     window.columnconfigure(1, weight=3)
    #     # nickname
    #     nickname_label = ttk.Label(window, text="Nickname:")
    #     nickname_label.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

    #     nickname_entry = ttk.Entry(window)
    #     nickname_entry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

    #     # name
    #     name_label = ttk.Label(window, text="Name:")
    #     name_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

    #     name_entry = ttk.Entry(window)
    #     name_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

    #     # email
    #     email_label = ttk.Label(window, text="Email:")
    #     email_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

    #     email_entry = ttk.Entry(window)
    #     email_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

    #     # save button
    #     save_button = ttk.Button(window, text="Save")
    #     save_button.grid(column=0, row=3, sticky=tk.SW, padx=5, pady=5)

    #     # cancel button
    #     cancel_button = ttk.Button(window, text="Cancel", command=window.destroy)
    #     cancel_button.grid(column=1, row=3, sticky=tk.SE, padx=5, pady=5)
    #     window.focus()
    #     window.grab_set() # Modal.


    # def menu_about():
    #     messagebox.showinfo('About', 'Demo on Upskill course')


root = MainWindow()
root.mainloop()