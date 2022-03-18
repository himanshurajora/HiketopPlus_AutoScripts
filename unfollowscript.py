import pyautogui
import time
time.sleep(3)

for i in range(12):
    pyautogui.click(1101,210 + (68*(i+1)))
    time.sleep(0.1)