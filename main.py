import klistener
import mlistener
import pynput
from screenshooter import take_screnshot

klistener.start_klist()
with pynput.mouse.Listener(on_click=mlistener.click, on_move = mlistener.mmove) as mmlistener:
    mmlistener.join()
    mmlistener.wait()
take_screnshot(mlistener.x0,mlistener.y0,mlistener.x1,mlistener.y1)
