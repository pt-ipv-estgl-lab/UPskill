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
