import pyautogui, os
from time import sleep

os.startfile("notepad.exe")
sleep(1)
pyautogui.click()
pyautogui.write("Hey, I am Orange!")