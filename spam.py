import pyautogui 
import time

time.sleep(5)

est = open("spam")

for v in est:

   pyautogui.typewrite(v, interval=0.02)
   pyautogui.press("enter")