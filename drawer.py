import win32con
import win32gui
import win32ui
import win32api
import win32com
from ctypes import windll

import mlistener

dev_con = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dev_con)
hwnd = win32gui.WindowFromPoint((0, 0))
monitor = (0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1))

white = win32api.RGB(255, 0, 0)

# def draw_rect(x0,y0,x1,y1):




def draw_rect():

    x0, y0 = win32api.GetCursorPos()
    x1, y1 = x0, y0
    mlistener.start_mlist()
    while mlistener.mouse_pressed:
        win32gui.SetCapture(hwnd)
        rect = win32gui.DrawEdge(dev_con, (x0, y0, x1, y1), win32con.EDGE_BUMP, win32con.BF_RECT)
        if win32con.WM_MOUSEMOVE:
            x1,y1 = win32api.GetCursorPos()
            # rect = win32gui.DrawEdge(dev_con, (x0,y0,x1,y1), win32con.EDGE_BUMP, win32con.BF_RECT)
            win32gui.InvalidateRect(hwnd,monitor,True)
        if not mlistener.mouse_pressed:
            x1,y1 = win32api.GetCursorPos()
            # rect = win32gui.DrawEdge(dev_con, (x0, y0, x1, y1), win32con.EDGE_BUMP, win32con.BF_RECT)
            win32gui.InvalidateRect(hwnd, monitor, True)
            mlist.stop()