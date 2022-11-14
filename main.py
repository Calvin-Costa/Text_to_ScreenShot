import klistener
import mlistener
import pynput


klistener.start_klist()
with pynput.mouse.Listener(on_click=mlistener.click, on_move = mlistener.mmove) as mmlistener:
    mmlistener.join()
    mmlistener.wait()

