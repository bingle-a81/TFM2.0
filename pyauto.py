import pyautogui as py
import os
from time import sleep
import keyboard
from ctypes import windll
import win32api
import TFM_settings

# sleep=time.sleep(5)
picture_folder=r'.picture\\'

def double_click(point,):
    py.moveTo(point)
    py.doubleClick(point,button='LEFT',duration=0.25)

def left_click(point,):
    py.moveTo(point, duration=0.25)
    py.leftClick(point, duration=0.25)

def click(lst:list,region=(50,50,400,400)):
    ls_loc=[]
    for x in lst:
        try:
            a=py.locateOnScreen(os.path.join(picture_folder,x),region=region, confidence=0.95)
        except:
            continue
        ls_loc.append(a)
    if ls_loc:
        double_click(ls_loc[0])
    else:
        return False
    left_click((719, 400))
    return True


def trans_nc_explorer(machine):
    path = r"C:\Users\Public\Desktop\NC Explorer"
    path = os.path.realpath(path)
    os.startfile(path)
    sleep(5)
    keyboard.press_and_release('win + up')
    sleep(3)  
    if machine!='Nomura NN-20J3XB80(6)':
        a=os.path.join(picture_folder, 'subnet.png')
        double_click(py.locateOnScreen(a,region=(100,100,400,400), confidence=0.5))
        left_click((719, 400))
        lst=[(TFM_settings.picture(machine.strip())),
             ('cnc_mem1.png','cnc_mem2.png','cnc_mem3.png','cnc_mem4.png','cnc_mem5.png','cnc_mem6.png'),
            ('prg1.png','prg2.png','prg3.png','prg4.png'),
             ('user1.png','user2.png','user3.png','user4.png'),
        ]

        for x in lst:
            click(x)
        if click(('imya.png',),)!=True:
            click(('kolonki.png','kolonki1.png'),region=(1500,800,1920,1080))

        if click(('data_norm.png',),)!=True:
            click(('data.png',),region=(800,50,1200,250))

        lst=[]





if __name__ == '__main__':
    trans_nc_explorer('Nomura NN-20J2(1)')

    quit(-1)




# import  AppOpener

# AppOpener.open("yandex")
# time.sleep(5)
# keyboard.press_and_release('win + up')
# time.sleep(5)
# AppOpener.close("yandex", match_closest=True, output=False)
# path = r"C:\Users\Public\Desktop\NC Explorer"
# path = os.path.realpath(path)
# os.startfile(path)
# sleep
# keyboard.press_and_release('win + up')
# sleep


# if windll.user32.OpenClipboard(None):
#     windll.user32.EmptyClipboard()
#     windll.user32.CloseClipboard()
#     print(9)

# time.sleep(5)
# print(py.position())
# quit(-1)
# keyboard.press_and_release('shift+s, space')


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

# keyboard.wait('space')
# print (win32api.GetCursorPos())