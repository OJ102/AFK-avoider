import tkinter as tk
from tkinter import ttk




class Window:
    loop=True
    def __init__(self):
        # Initializes
        self.root = tk.Tk()

        # Sets geometry and blocks resizing
        self.root.geometry("300x150")
        self.root.title("AFK Avoider")
        self.root.resizable(False, False)

        # Makes a label asking "Are you back?"
        self.label = tk.Label(
                                self.root, 
                                text = "Are you back?", 
                                font = ("Times New Roman", 15)
                                )
        self.label.pack(pady = 20)

        # Makes a grid
        self.button_frame = tk.Frame(self.root)
        self.button_frame.columnconfigure(0, weight = 1)
        self.button_frame.columnconfigure(1, weight = 1)

        # Adds two buttons "Yes" and "No" to the grid
        self.yes_button = tk.Button(
                                    self.button_frame, 
                                    text = "Yes", 
                                    font = ("Times New Roman", 15), 
                                    width = 5, 
                                    command = self.yes
                                    )
        self.yes_button.grid(row = 0, column = 0, ipadx = 10)
        self.no_button = tk.Button(
                                    self.button_frame, 
                                    text = "No", 
                                    font = ("Times New Roman", 15), 
                                    width = 5, 
                                    command = self.no
                                    )
        self.no_button.grid(row = 0, column = 1, ipadx = 10)

        # Puts the grid onto the root window
        self.button_frame.pack(fill = "x")

        # Destroy after feature
        secs_to_kill = 5000
        self.destroy_after = self.root.after(secs_to_kill, self.root.destroy)

        # Display the root window
        self.root.mainloop()


    def yes(self):
        self.root.destroy()
        Window.loop = False


    def no(self):
        self.root.destroy()

