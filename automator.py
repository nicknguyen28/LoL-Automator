import pyautogui
from time import sleep
# pyautogui.FAILSAFE = True

while True:
    print("Looping!")
    if (pyautogui.position().x == 0 and pyautogui.position().y == 0):
        print("Ending program!")
        break
    acceptXY = pyautogui.locateCenterOnScreen("accept.png", confidence = 0.5)
    if acceptXY != None:
        pyautogui.moveTo(acceptXY, duration = 0.5)
    sleep(3)