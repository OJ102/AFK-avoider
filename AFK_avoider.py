from mouse import Mouse
from window import Window




cursor = Mouse()

while Window.loop:
    cursor.random_pos()
    cursor.move_to()

    if cursor.is_moving():  # Checks if the user is moving the mouse
        popup = Window()