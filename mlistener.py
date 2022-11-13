import pynput
import win32api

import drawer
mouse_pressed = 0
x0 = y0 = x1 = y1 = 0
def click(x, y,button, pressed):
    global x0, y0, x1, y1
    global mouse_pressed
    if pressed:
        mouse_pressed = win32api.GetKeyState(0x01)
        print(mouse_pressed)
        drawer.draw_rect()
    if not pressed:
        print('teste')
        # x1 = x
        # y1 = y
        mouse_pressed = win32api.GetKeyState(0x01)
        print(mouse_pressed)
        return False


def mmove(x,y):
    global x1, y1, mouse_pressed
    x1, y1 = win32api.GetCursorPos()
    # if win32api.GetKeyState(0x01) < 0:
    #     mouse_pressed = win32api.GetKeyState(0x01)
