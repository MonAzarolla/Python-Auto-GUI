#Creating a bot on microsoft paint that draws (following a tutorial on youtube)

import pyautogui
import time

pyautogui.mouseDown(500,200, button="left")
pyautogui.moveTo(600,100,8)
pyautogui.mouseUp()
pyautogui.moveTo(600,200,10)

time.sleep(1)

distance = 400

while distance > 0: 
    pyautogui.dragRel(distance,1,7, button ="left")
    pyautogui.dragRel(distance,5,button = "left")
    distance = distance -10 
    pyautogui.dragRel(0, -distance, 1, button = "left")
time.sleep(2)



