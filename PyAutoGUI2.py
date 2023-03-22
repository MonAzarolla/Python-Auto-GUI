import pyautogui 
import time
# 1) This will be printing the size of the screen aka the resolution of your screen

print(pyautogui.size()) 

# 2) This here will print the current position of the mouse. 


print(pyautogui.position())

# 3) This will give the file time before it continues 

time.sleep(3)

# 4) Here you will get Python to move your mouse (3 seconds)

pyautogui.moveTo(100,100,3)

# 5) This will move the mouse where the current position of the mouse is, relative to that. 

pyautogui.moveRel (100,100,3)

# 6) Now we will get python to make our mouse click. 

pyautogui.click(100,100,3,3 button = "left")

pyautogui.leftClick

pyautogui.rightClick 

pyautogui.tripleClick

pyautogui.doubleClick

# These are all the different commands you can use. 

# 7) Python make your computer scroll 

pyautogui.scroll(500)

# This moves up 

# This moves down 

pyautogui.scroll(-500)

# 8) Mouse up and down for Python 

pyautogui.mouseUp(100,100, buttom ="left")

pyautogui.mouseDown(100,100, buttom = "left" )

# 9 Here is an example of mouse up and down 

pyautogui.mouseDown(200,600, button="left")

pyautogui.moveTo(800,600,6)
pyautogui.mouseUp()
pyautogui.moveTo(1000,400)

#It will happen in a instant and it is the nicest way to do it as it is running for over 6 seconds. 

# You can make it move your mouse up and mouse down and make modifications. 


