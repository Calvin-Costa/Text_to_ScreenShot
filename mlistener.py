import pynput

import drawer
mouse_pressed = False
x0 = y0 = x1 = y1 = 0
def click(x, y,button, pressed):
    global x0, y0, x1, y1
    global mouse_pressed
    if pressed:
        x0 = x
        y0 = y
        mouse_pressed = True
    if not pressed:
        x1 = x
        y1 = y
        mouse_pressed = False
        return False

def mmove(x,y):
    global x1, y1
    x1 = x
    y1 = y

def start_mlist():
    mlist = pynput.mouse.Listener(on_click=click,on_move=mmove)
    mlist.start()
    mlist.join()
    mlist.wait()

