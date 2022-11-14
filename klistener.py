from pynput import keyboard

def kpress(key):
    pass


def krelease(key):
    if key == keyboard.Key.shift_l:
        return False



def start_klist():
    klist = keyboard.Listener(on_press=kpress, on_release=krelease)
    klist.start()
    klist.join()
    klist.wait()
    klist.stop()
