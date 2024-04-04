import pyautogui as py
import os,time
import keyboard
from ctypes import windll

import  AppOpener

AppOpener.open("yandex")
time.sleep(5)
keyboard.press_and_release('win + up')
time.sleep(5)
AppOpener.close("yandex", match_closest=True, output=False)
# path = r"C:\Users\Public\Desktop\NC Explorer"
# path = os.path.realpath(path)
# os.startfile(path)
# time.sleep(3)
# keyboard.press_and_release('win + up')

# if windll.user32.OpenClipboard(None):
#     windll.user32.EmptyClipboard()
#     windll.user32.CloseClipboard()
#     print(9)

# time.sleep(5)
# print(py.position())
quit(-1)
# keyboard.press_and_release('shift+s, space')
# py.useImageNotFoundException()
# py.useImageNotFoundException()

# time.sleep(5)
# print(py.position())

a=r'.picture\Screenshot_1.png'
# if os.path.isfile(a):
#     print('jk')
#     a = os.path.realpath(a)
#     # os.startfile(a)
a = os.path.realpath(a)
print(a)
b=py.locateOnScreen(a,region=(107,103,500,500), confidence=0.95)
print(b)
# ,region=(170,200,270,300), confidence=0.95

# .locateOnScreen(x,region=(164,104,240,200), confidence=0.95)
py.moveTo(b)
print(py.position())