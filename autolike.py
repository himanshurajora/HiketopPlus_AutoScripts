import pyautogui
import time
from mousepos import *
import followcheck

poses = [[1000,995], [913, 460],[1203, 30],[1804, 45]]

def like():
    fails = 0
    for i in range(61):
        if(followcheck.checklikefail()== True):
            fails = fails + 1
            pyautogui.click(1000,995)
            time.sleep(0.5)
        pyautogui.click(1000,995)
        time.sleep(4)
        pyautogui.doubleClick(913, 460,0.1)
        time.sleep(0.5)
        pyautogui.click(1203, 30)
        pos = queryMousePosition()
        p = []
        p.append(int(pos['x'] * 1.5))
        p.append(int(pos['y'] * 1.5))
        if(p not in poses):
            return
        time.sleep(5)
    
    fails = 0
    for i in range(fails):
        if(followcheck.checklikefail()== True):
            fails = fails + 1
            pyautogui.click(1000,995)
            time.sleep(0.5)
        pyautogui.click(1000,995)
        time.sleep(4)
        pyautogui.doubleClick(913, 460,0.1)
        time.sleep(0.5)
        pyautogui.click(1203, 30)
        pos = queryMousePosition()
        p = []
        p.append(int(pos['x'] * 1.5))
        p.append(int(pos['y'] * 1.5))
        if(p not in poses):
            return
        time.sleep(5)
    
    fails = 0
    for i in range(fails):
        if(followcheck.checklikefail()== True):
            fails = fails + 1
            pyautogui.click(1000,995)
            time.sleep(0.5)
        pyautogui.click(1000,995)
        time.sleep(4)
        pyautogui.doubleClick(913, 460,0.1)
        time.sleep(0.5)
        pyautogui.click(1203, 30)
        pos = queryMousePosition()
        p = []
        p.append(int(pos['x'] * 1.5))
        p.append(int(pos['y'] * 1.5))
        if(p not in poses):
            return
        time.sleep(5)

like()