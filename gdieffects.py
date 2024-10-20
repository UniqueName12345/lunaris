import ctypes
import math
import random
import time

def RGB(r, g, b):
    """Creates a COLORREF value from red, green, blue components."""
    return (b << 16) | (g << 8) | r

user32 = ctypes.windll.user32
w = user32.GetSystemMetrics(0)
h = user32.GetSystemMetrics(1)

def bouncing_balls():
    sign_x = 1
    sign_y = 1
    incrementor = 10
    x = 10
    y = 10
    while True:
        hdc = user32.GetDC(0)
        x += incrementor * sign_x
        y += incrementor * sign_y
        top_x = 0 + x
        top_y = 0 + y
        bottom_x = 100 + x
        bottom_y = 100 + y
        brush = ctypes.windll.gdi32.CreateSolidBrush(RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        ctypes.windll.gdi32.SelectObject(hdc, brush)
        ctypes.windll.gdi32.Ellipse(hdc, top_x, top_y, bottom_x, bottom_y)
        if y >= h:
            sign_y = -1
        if x >= w:
            sign_x = -1
        if y <= 0:
            sign_y = 1
        if x <= 0:
            sign_x = 1
        time.sleep(0.01)
        ctypes.windll.gdi32.DeleteObject(brush)
        user32.ReleaseDC(0, hdc)

def bitblt222():
    while True:
        hdc = user32.GetDC(0)
        x = user32.GetSystemMetrics(0)
        y = user32.GetSystemMetrics(1)
        w = user32.GetSystemMetrics(0)
        h = user32.GetSystemMetrics(1)
        ctypes.windll.gdi32.BitBlt(hdc, random.randint(0, 222), random.randint(0, 222), w, h, hdc, random.randint(0, 222), random.randint(0, 222), 0x00110066)
        time.sleep(0.01)
        user32.ReleaseDC(0, hdc)
