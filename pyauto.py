import pyautogui as py
import os,time

# py.useImageNotFoundException()

# time.sleep(5)
# print(py.position())

a=r'c:\Users\breat\.picture\Screenshot_1.png'
# if os.path.isfile(a):
#     print('jk')
#     a = os.path.realpath(a)
#     # os.startfile(a)
a = os.path.realpath(a)
print(a)
b=py.locateOnScreen(a,region=(170,200,500,500), confidence=0.5)
print(b)
# ,region=(170,200,270,300), confidence=0.95

# .locateOnScreen(x,region=(164,104,240,200), confidence=0.95)
py.moveTo(470,400)
