import pyautogui
import time
from ctypes import windll, Structure, c_long, byref
from PIL import Image, ImageGrab
from mousepos import *
import followcheck

def refreshpage():
    for l in range(8):
        pyautogui.scroll(5, 0, 30) 

def follow():
    refreshpage()
    time.sleep(5)

    for i in range(3):
        time.sleep(0.2)
        for j in range(3):
            time.sleep(0.2)
            if(followcheck.limitend() == True):
                return
            if(i == 0):
                if(j is not 2):
                    pyautogui.click(918 + (190 * (j)),381 +(260 *(i)))
            else:
                pyautogui.click(728 + (190 * (j)),381 +(260 *(i)))
                if(followcheck.limitend() == True):
                    return
            time.sleep(2)
            point = followcheck.scanfollow()
            if(point != None):
                pyautogui.click(point[0] + 50, point[1] + 7)
            time.sleep(0.5)
            pyautogui.click(1203, 30)
            time.sleep(0.4)
            if(followcheck.limitend() == True):
                return
                
    pyautogui.moveTo(920,361)
    follow()

follow()