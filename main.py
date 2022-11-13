import win32con
import win32gui
import win32ui
import win32api

import klistener
import mlistener
import pynput
from pynput import keyboard
from pynput import mouse

# for y in range(100):
#     win32gui.SetPixel(dev_con, 100, 100 + y, white)


klistener.start_klist()
with pynput.mouse.Listener(on_click=mlistener.click, on_move = mlistener.mmove) as mmlistener:
    mmlistener.join()
    mmlistener.wait()

