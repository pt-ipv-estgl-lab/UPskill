import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class GUI_Friends:
    def __init__(self, root_container) -> None:
        self.__root = root_container
        
    def create_tree_frame(self, container):

        frame = ttk.Frame(container)
        frame.columnconfigure(0, weight=4)
        
        # define columns
        columns = ('nickname', 'name', 'email')

        tree = ttk.Treeview(frame, columns=columns, show='headings')

        # define headings
        tree.heading('nickname', text='Nickname')
        tree.heading('name', text='Name')
        tree.heading('email', text='Email')

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')        

        return frame
    
    def create_buttons_frame(self, container):
        frame = ttk.Frame(container)

        frame.columnconfigure(0, weight=1)

        ttk.Button(frame, text='Create', command=self.open_friend_window).grid(column=0, row=0)
        ttk.Button(frame, text='Retrieve').grid(column=0, row=1)
        ttk.Button(frame, text='Update').grid(column=0, row=2)
        ttk.Button(frame, text='Delete').grid(column=0, row=3)

        for widget in frame.winfo_children():
            widget.grid(padx=5, pady=5)

        return frame        
    
    def create_main_container(self):

        frame = ttk.Frame(self.__root)

        # layout on the main container
        frame.columnconfigure(0, weight=4)
        frame.columnconfigure(1, weight=1)

        __tree_frame = self.create_tree_frame(frame)
        __tree_frame.grid(column=0, row=0)

        __buttons_frame = self.create_buttons_frame(frame)
        __buttons_frame.grid(column=1, row=0)

        frame.pack()
        return frame

    def open_friend_window(self):
        self.__friend_window = FriendWindow()

class FriendWindow(tk.Toplevel):
    def __init__(self, center_x=120,center_y=100, *args, **kargs):
        super().__init__(*args, **kargs)
        # Create secondary (or popup) window.
        self.title('Friend')
        self.geometry(f'300x200+{center_x}+{center_y}')
        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        # nickname
        nickname_label = ttk.Label(self, text="Nickname:")
        nickname_label.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

        nickname_entry = ttk.Entry(self)
        nickname_entry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

        # name
        name_label = ttk.Label(self, text="Name:")
        name_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

        name_entry = ttk.Entry(self)
        name_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        # email
        email_label = ttk.Label(self, text="Email:")
        email_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

        email_entry = ttk.Entry(self)
        email_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

        # save button
        save_button = ttk.Button(self, text="Save")
        save_button.grid(column=0, row=3, sticky=tk.SW, padx=5, pady=5)

        # cancel button
        cancel_button = ttk.Button(self, text="Cancel", command=self.destroy)
        cancel_button.grid(column=1, row=3, sticky=tk.SE, padx=5, pady=5)
        self.focus()
        self.grab_set() # Modal.

if __name__ == '__main__': # for testing propose
    root = tk.Tk()
    root.title('Treeview demo')
    root.geometry('720x280')
    manange_friends = GUI_Friends(root)
    manange_friends.create_main_container()
    root.mainloop()
