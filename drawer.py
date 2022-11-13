import win32con
import win32gui
import win32ui
import win32api
import win32com
from ctypes import windll
import pynput
import mlistener

monitor = (0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1))
dev_con = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dev_con)
hwnd = win32gui.WindowFromPoint((0, 0))

def draw_rect():
    # with pynput.mouse.Listener(on_move=mlistener.mmove, on_click=mlistener.click) as listener:
    #     listener.join()
    #     listener.wait()
    if mlistener.mouse_pressed >= 0:
        x0, y0 = win32api.GetCursorPos()
        print('Agora estou indo para o ciclo while')
        print(mlistener.mouse_pressed)
        if mlistener.mouse_pressed >= 0:
            drawing = True
        while drawing:
            # print(win32gui.GetCapture())
            # rect = win32gui.DrawEdge(dev_con, (x0, y0, x1, y1), win32con.EDGE_BUMP, win32con.BF_RECT)
            # x1, y1 = win32api.GetCursorPos()
            print(mlistener.x1,mlistener.y1)
            rect = win32gui.DrawEdge(dev_con, (x0, y0, mlistener.x1,mlistener.y1), win32con.EDGE_BUMP, win32con.BF_RECT)
            win32gui.InvalidateRect(hwnd, monitor, True)
            if win32api.GetKeyState(0x01) < 0:
                drawing = False
                # mlistener.mouse_pressed = -127

