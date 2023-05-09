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

#Tkinter function to display a pop up to kill the script
def popup():
    root=tk.Tk()
    root.geometry("300x150")
    root.title("AFK avoider")
    root.resizable(False, False)

    label=tk.Label(root,text="Are you back?",font=("times new roman",15))
    label.pack(pady=20)

    buttonframe=tk.Frame(root)
    # buttonframe=ttk.Frame(root,padding=10)
    buttonframe.columnconfigure(0,weight=1)
    buttonframe.columnconfigure(1,weight=1)


    button1=tk.Button(buttonframe,text="Yes",font=("times new roman",15),width=5)
    button1.grid(row=0,column=0,ipadx=10)
    button2=tk.Button(buttonframe,text="No",font=("times new roman",15),width=5)
    button2.grid(row=0,column=1,ipadx=10)

    

    buttonframe.pack(fill="x")

    root.mainloop()
    

popup()


# while True:
#     if ismoving():#Checks if the user is moving the mouse
#         break
#     x=random.randint(800,1000)
#     y=random.randint(400,600)
#     pgui.moveTo(x,y,0.5)#check functioning
    


