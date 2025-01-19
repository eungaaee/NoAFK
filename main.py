import pyautogui
import random
import time

screenWidth, screenHeight = pyautogui.size()
interval = 60
dur = 3

while True:
    rw = random.randint(1, screenWidth)
    rh = random.randint(1, screenHeight)
    pyautogui.moveTo(rw, rh, dur)
    pyautogui.press('scrolllock')
    time.sleep(interval)