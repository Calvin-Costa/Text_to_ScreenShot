import pynput
import win32api

import drawer
mouse_pressed = False
x0 = y0 = x1 = y1 = 0
counter = 0
def click(x, y,button, pressed):
    global x0, y0, x1, y1, counter
    global mouse_pressed
    if pressed:
        x0,y0 = win32api.GetCursorPos()
        mouse_pressed = True
        print(mouse_pressed)
        counter += 1
    if not pressed:
        # x1 = x
        # y1 = y
        mouse_pressed = False



def mmove(x,y):
    global x0,y0,x1, y1, mouse_pressed, counter
    if mouse_pressed:
        x1, y1 = win32api.GetCursorPos()
        drawer.draw_rect(x0, y0, x1, y1)

    if mouse_pressed and counter > 1:
        print(mouse_pressed)
        return False

    # if win32api.GetKeyState(0x01) < 0:
    #     mouse_pressed = win32api.GetKeyState(0x01)
