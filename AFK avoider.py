#AFK avoider
import pyautogui as pgui
import random
import time
import tkinter as tk
from tkinter import ttk


class mouse:
    speed=0.5
    def __init__(self) :
        Position=pgui.position()
        
        #Assign to self
        self.x=Position[0]
        self.y=Position[1]

    def Random_Pos(self):
        x=random.randint(800,1000)
        y=random.randint(400,600)
        self.x=x
        self.y=y
    
    def Move_To(self):
        x=self.x
        y=self.y
        speed=self.speed
        pgui.moveTo(x,y,speed)

    def is_moving(self):#Checks if the cursor is moving
        initial=pgui.position()
        time.sleep(1)
        final=pgui.position()

        if initial[0]==final[0] and initial[1]==final[1]:   
            return False
        else:
            return True

    def Display_Mouse_Pos(self):
        x=self.x
        y=self.y
        print(f"(x={x}, y={y})")





#Tkinter function to display a pop up to kill the script
class window:

    def __init__(self) -> None:
        #Initializes
        self.root=tk.Tk()

        #Sets geometry and blocks resizing
        self.root.geometry("300x150")
        self.root.title("AFK avoider")
        self.root.resizable(False, False)

        #Makes a label asking are you back
        self.label=tk.Label(self.root,text="Are you back?",font=("times new roman",15))
        self.label.pack(pady=20)

        #Makes a grid
        self.buttonframe=tk.Frame(self.root)
        self.buttonframe.columnconfigure(0,weight=1)
        self.buttonframe.columnconfigure(1,weight=1)

        #Adds 2 buttons yes and no to the grid
        self.Yes_Button=tk.Button(self.buttonframe,text="Yes",font=("times new roman",15),width=5,command=self.yes)
        self.Yes_Button.grid(row=0,column=0,ipadx=10)
        self.No_Button=tk.Button(self.buttonframe,text="No",font=("times new roman",15),width=5,command=self.no)
        self.No_Button.grid(row=0,column=1,ipadx=10)

        #Puts the grid on to the root window
        self.buttonframe.pack(fill="x")

        #Destroy after feature
        Secs_To_Destroy=5000
        self.Destroy_After= self.root.after(Secs_To_Destroy, self.root.destroy)


        #Display the root window
        self.root.mainloop()

 
    
    def yes(self):
        self.root.destroy()
        global run 
        run = False

    def no(self):
        self.root.destroy()   



    pass



 

run=True
cursor=mouse()
while run:
    cursor.Random_Pos()
    cursor.Move_To()
    if cursor.is_moving():#Checks if the user is moving the mouse
        popup=window()

