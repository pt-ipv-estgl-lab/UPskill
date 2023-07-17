import tkinter as tk
from tkinter import ttk


def open_secondary_window():
    # Create secondary (or popup) window.
    secondary_window = tk.Toplevel()
    secondary_window.title("Secondary Window")
    secondary_window.config(width=300, height=200)
    # Create a button to close (destroy) this window.
    button_close = ttk.Button(
        secondary_window,
        text="Close window",
        command=secondary_window.destroy
    )
    button_close.place(x=75, y=75)


# Create the main window.
main_window = tk.Tk()
main_window.config(width=400, height=300)
main_window.title("Main Window")
# Create a button inside the main window that
# invokes the open_secondary_window() function
# when pressed.
button_open = ttk.Button(
    main_window,
    text="Open secondary window",
    command=open_secondary_window
)
button_open.place(x=100, y=100)
main_window.mainloop()