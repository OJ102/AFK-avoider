#AFK avoider
import pyautogui as pgui
import random
import time
import tkinter as tk
from tkinter import ttk

def ismoving():#Checks if the cursor is moving
    initial=pgui.position()
    time.sleep(1)
    final=pgui.position()

    print(initial)
    print(final)
    if initial[0]==final[0] and initial[1]==final[1]:   
        return False
    else:
        return True

#command function



run=True


#Tkinter function to display a pop up to kill the script
def popup():
    #Initializes
    root=tk.Tk()

    def yes():
        root.destroy()
        global run 
        run = False

    def no():
        root.destroy()

    #Sets geometry and blocks resizing
    root.geometry("300x150")
    root.title("AFK avoider")
    root.resizable(False, False)

    #Makes a label asking are you back
    label=tk.Label(root,text="Are you back?",font=("times new roman",15))
    label.pack(pady=20)

    #Makes a grid
    buttonframe=tk.Frame(root)
    buttonframe.columnconfigure(0,weight=1)
    buttonframe.columnconfigure(1,weight=1)

    #Adds 2 buttons yes and no to the grid
    Yes_Button=tk.Button(buttonframe,text="Yes",font=("times new roman",15),width=5,command=yes)
    Yes_Button.grid(row=0,column=0,ipadx=10)
    No_Button=tk.Button(buttonframe,text="No",font=("times new roman",15),width=5,command=no)
    No_Button.grid(row=0,column=1,ipadx=10)

    #Puts the grid on to the root window
    buttonframe.pack(fill="x")

    cancel_id = root.after(5000, root.destroy)

    #Displays the root window
    root.mainloop()    
    


while run:
    if ismoving():#Checks if the user is moving the mouse
        popup()
    x=random.randint(800,1000)
    y=random.randint(400,600)
    pgui.moveTo(x,y,0.5)#check functioning
    
class mouse:
    def __init__(self,x=950,y=500) -> None:
        self.x=x
        self.y=y
        pass 
    
    pass