import keyboard
import win32api        


keyboard.wait('space')
print (win32api.GetCursorPos())     