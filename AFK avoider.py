#AFK avoider
import pyautogui as pgui
import random
import time
import tkinter as tk

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
    root.geometry("400x200")
    root.title("AFK avoider")

    label=tk.Label(root,text="Are you back?",font=("times new roman",20))
    label.pack(pady=20)

    button1=tk.Button(root,text="Yes",font=("times new roman",20))
    button1.pack(padx=10,pady=10)
    button2=tk.Button(root,text="No",font=("times new roman",20))
    button2.pack(padx=10,pady=10)
    root.mainloop()
    

popup()


# while True:
#     if ismoving():#Checks if the user is moving the mouse
#         break
#     x=random.randint(800,1000)
#     y=random.randint(400,600)
#     pgui.moveTo(x,y,0.5)#check functioning
    


