import pyautogui
import time


print("This code is running")


while True:

    pyautogui.typewrite("Your text")
    
    pyautogui.press("space")

    time.sleep(1.0)