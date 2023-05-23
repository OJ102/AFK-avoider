import pyautogui as pgui
import random
import time



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
