import win32con
import win32gui
import win32ui
import win32api


monitor = (0, 0, win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1))
dev_con = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dev_con)
hwnd = win32gui.WindowFromPoint((0, 0))

def draw_rect(x0,y0,x1,y1):
    print(f"({x0},{y0}),({x1},{y1})")
    rect = win32gui.DrawEdge(dev_con, (x0, y0,x1,y1), win32con.EDGE_BUMP, win32con.BF_RECT)
    win32gui.InvalidateRect(hwnd, monitor, True)