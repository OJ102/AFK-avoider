import pyautogui as pgui
import random
import time
import tkinter as tk
from tkinter import ttk


class Mouse:
    speed = 0.5


    def __init__(self):
        position = pgui.position()

        # Assign to self
        self.x = position[0]
        self.y = position[1]


    def random_pos(self):
        x = random.randint(800, 1000)
        y = random.randint(400, 600)
        self.x = x
        self.y = y


    def move_to(self):
        x = self.x
        y = self.y
        speed = self.speed
        pgui.moveTo(x, y, speed)


    def is_moving(self):  # Checks if the cursor is moving
        initial = pgui.position()
        time.sleep(1)
        final = pgui.position()

        if initial[0] == final[0] and initial[1] == final[1]:
            return False
        else:
            return True


    def display_mouse_pos(self):
        x = self.x
        y = self.y
        print(f"(x = {x}, y = {y})")


class Window:
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
                                    command=self.no
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
        global run
        run = False

 
    def no(self):
        self.root.destroy()


run = True
cursor = Mouse()
while run:
    cursor.random_pos()
    cursor.move_to()
    
    if cursor.is_moving():  # Checks if the user is moving the mouse
        popup = Window()
