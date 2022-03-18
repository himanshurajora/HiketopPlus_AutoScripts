from ctypes import windll, Structure, c_long, byref
from time import sleep


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}


sleep(2)
pos = queryMousePosition()
pii = []
pii.append(int(pos['x'] * 1.5))
pii.append(int(pos['y'] * 1.5))
print(pii)  
