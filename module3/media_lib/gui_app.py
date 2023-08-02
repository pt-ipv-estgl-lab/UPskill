import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox
from gui_friends import GUI_Friends

class MainWindow(tk.Tk):
    def __init__(self, window_width = 640, window_height = 480, *args, **kargs):
        super().__init__(*args, **kargs)
        self.title("Media Lib App")
        self.__handler = None

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
        __management_menu.add_command(label='Products', command=self.manage_products)
        __management_menu.add_command(label='Friends', command=self.manage_friends)

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
            command=self.confirm_exit
        )
        self.config(menu=__menubar)

    def manage_products(self):
        if self.__handler != None:
            self.__handler.destroy()
            self.__handler = None
            
        messagebox.showinfo('Products', 'This will be the products management UI')

    def manage_friends(self):
        __manange_friends = GUI_Friends(self)
        self.__handler = __manange_friends.create_main_container()

        # messagebox.showinfo('Friends', 'This will be the friends management UI')

    def confirm_exit(self):
        if messagebox.askyesno('Are you sure', 'Quit App'):
            self.destroy()

root = MainWindow(1024,768)
root.mainloop()