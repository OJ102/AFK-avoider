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
        pgui.moveTo(x,y,speed)#check functioning

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


# def is_moving():#Checks if the cursor is moving
#     initial=pgui.position()
#     time.sleep(1)
#     final=pgui.position()

#     if initial[0]==final[0] and initial[1]==final[1]:   
#         return False
#     else:
#         return True


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

    #Destroy after feature
    Secs_To_Destroy=5000
    Destroy_After= root.after(Secs_To_Destroy, root.destroy)

    #Displays the root window
    root.mainloop()    
    

cursor=mouse()
while run:
    cursor.Random_Pos()
    cursor.Move_To()
    if cursor.is_moving():#Checks if the user is moving the mouse
        popup()


# cursor=mouse()
# cursor.Display_Mouse_Pos()
# cursor.Random_Pos()
# cursor.Display_Mouse_Pos()
# print(cursor.is_moving())
# `