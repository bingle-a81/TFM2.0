import keyboard
import win32api 
import os    
import AppOpener   
import time


# keyboard.wait('space')
# print (win32api.GetCursorPos())      

AppOpener.open("filecontrol")  
time.sleep(5)
AppOpener.close("filecontrol")                                        