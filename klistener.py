import pynput
from pynput import keyboard

import drawer
import mlistener


def kpress(key):
    pass


def krelease(key):
    if key == keyboard.Key.shift_l:
        drawer.draw_rect()



def start_klist():
    klist = keyboard.Listener(on_press=kpress, on_release=krelease)
    klist.start()
    klist.join()
    klist.wait()

