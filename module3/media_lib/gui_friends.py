import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from tkinter import simpledialog
from friend import Friend, FriendError

class GUI_Friends:
    def __init__(self, root_container) -> None:
        self.__root = root_container
        
    def create_tree_frame(self, container):

        frame = ttk.Frame(container)
        frame.columnconfigure(0, weight=4)
        
        # define columns
        columns = ('nickname', 'name', 'email')

        self.__tree = ttk.Treeview(frame, columns=columns, show='headings')

        # define headings
        self.__tree.heading('nickname', text='Nickname')
        self.__tree.heading('name', text='Name')
        self.__tree.heading('email', text='Email')

        self.__tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.__tree.yview)
        self.__tree.configure(yscroll=scrollbar.set)
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

        tree_frame = self.create_tree_frame(frame)
        tree_frame.grid(column=0, row=0)

        buttons_frame = self.create_buttons_frame(frame)
        buttons_frame.grid(column=1, row=0)

        frame.grid(column=0, row=0)
        return frame

    def open_friend_window(self):
        friend_window = FriendDialog(title='Friend', 
                                            parent=self.__root)
        if friend_window.friend != None:
            result = (friend_window.friend.get_nickname(), friend_window.friend.get_name(), 
                      friend_window.friend.get_email())
            showinfo("Result", str(result))
            self.__tree.insert('',
                               tk.END,
                               values=result)


class FriendDialog(tk.simpledialog.Dialog):
    def __init__(self, parent, title): 
        self.friend = None
        super().__init__(parent, title)

    def body(self, frame):
        container = ttk.Frame(frame)
        # configure the grid
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=3)
        # nickname
        nickname_label = ttk.Label(container, text="Nickname:")
        nickname_label.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

        self.__nickname_entry = ttk.Entry(container)
        self.__nickname_entry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

        # name
        name_label = ttk.Label(container, text="Name:")
        name_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

        self.__name_entry = ttk.Entry(container)
        self.__name_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

        # email
        email_label = ttk.Label(container, text="Email:")
        email_label.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)

        self.__email_entry = ttk.Entry(container)
        self.__email_entry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
        container.pack()
        self.__nickname_entry.focus_force()
        self.bind('<Return>', lambda event: self.save_click())
        self.bind('<Escape>', lambda event: self.destroy())
        return frame
    
    def save_click(self):
        try:
            self.friend = Friend(self.__nickname_entry.get(),
                             self.__name_entry.get(),
                             self.__email_entry.get())
            self.destroy()
        except FriendError as e:
            showerror('Friend Creator Error', str(e))
        

    def buttonbox(self):        
        # save button
        self.save_button = ttk.Button(self, text="Save", command=self.save_click)
        self.save_button.pack(side='left', padx=5, pady=5)

        # cancel button
        self.cancel_button = ttk.Button(self, text="Cancel", command=self.destroy)
        self.cancel_button.pack(side='right', padx=5, pady=5)


if __name__ == '__main__': # for testing propose
    root = tk.Tk()
    root.title('Treeview demo')
    root.geometry('720x280')
    manange_friends = GUI_Friends(root)
    manange_friends.create_main_container()
    root.mainloop()
