import pyautogui as py
import os
from time import sleep
import keyboard
from ctypes import windll
import win32api
from subprocess import Popen, PIPE
# -------------------
from logging_settings import set_logger
import TFM_settings
from py_functions import MachinePyautogui

# sleep=time.sleep(5)
py_log=set_logger('py_logger')
   
def trans_nc_explorer(machine):
    foo=MachinePyautogui()

    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()
        
    foo.open_folder_os(r"C:\Users\Public\Desktop\NC Explorer")
    sleep(5)
    if foo.find_picture(('kolonki.png','kolonki1.png'),region=(1800,900,1920,1050))==False:
        foo.hotkey('win + up')

    if machine!='Nomura NN-20J3XB80(6)':
        py_log.info('open subnet')
        foo.open_pic_folder(('subnet.png',),region=(100,100,400,400))

    lst=[(TFM_settings.picture(machine.strip())),
            ('cnc_mem1.png','cnc_mem2.png','cnc_mem3.png','cnc_mem4.png','cnc_mem5.png','cnc_mem6.png'),
        ('prg1.png','prg2.png','prg3.png','prg4.png'),
            ('user1.png','user2.png','user3.png','user4.png'), ]
    for x in lst:
        foo.open_pic_folder(x)

    sleep(10)    
    
    if foo.find_picture(('imya.png',))==False:
        foo.open_pic_folder( ('kolonki.png','kolonki1.png'),region=(1800,900,1920,1050),click=1)

    if foo.find_picture(['galka.png',],region=(695,120,750,150))==False:
        foo.open_pic_folder(('data.png',),region=(600,100,800,200),click=1)               

    foo.left_click((234, 172))  # первая программа
    sleep(1)
    keyboard.press('shift')
    sleep(1)
    foo.left_click((234, 518))  # последняя программа
    keyboard.release('shift')
    sleep(1)

    foo.hotkey('ctrl + c')

    sleep(1)
    foo.open_pic_folder(('vihod.png',),region=(1868,0,1915,40),click=1)
    foo.open_folder_os(os.path.join(TFM_settings.config.get_set_default('source'),machine))

    sleep(3)
    if foo.find_picture(('kolonki.png','kolonki1.png'),region=(1800,900,1920,1050))==False:
        foo.hotkey('win + up')

    foo.left_click((268, 558))    
    sleep(3)
    foo.hotkey('ctrl + v')
    sleep(3)
    if foo.find_picture(('konflicti.png',),region=(730,690,820,750))==True:
        foo.open_pic_folder(('konflicti.png',),region=(730,690,820,750),click=1)
        foo.open_pic_folder(('kopir_zamena.png',),region=(730,350,950,430),click=1)
    
    sleep(1)
    foo.left_click((860, 462))
    sleep(10)    
    foo.open_pic_folder(('vihod.png',),region=(1868,0,1915,40),click=1)
    sleep(2)
   
    py_log.info('программы скачаны')






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