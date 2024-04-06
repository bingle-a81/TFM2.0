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

# sleep=time.sleep(5)
py_log=set_logger('py_logger')
py.PAUSE=0.5

picture_folder=r'.picture\\nomura\\'

def double_click(point,):
    py.moveTo(point)
    py.doubleClick(point,button='LEFT',duration=0.25)
    

def left_click(point,):
    py.moveTo(point, duration=0.25)
    py.leftClick(point, duration=0.25)

def double(lst:list,region=(50,50,400,400)):
    ls_loc=[]
    for x in lst:
        try:
            # sleep(1)
            a=py.locateOnScreen(os.path.join(picture_folder,x),region=region, confidence=0.95)
            # sleep(1)
        except:
            continue
        ls_loc.append(a)
    if ls_loc:
        py_log.info(ls_loc[0])
        double_click(ls_loc[0])
    else:
        print('p')
        return False
    left_click((1300, 400))
    
    return True

def one_click(lst:list,region=(50,50,400,400)):
    ls_loc=[]
    for x in lst:
        try:
            a=py.locateOnScreen(os.path.join(picture_folder,x),region=region, confidence=0.95)
        except:
            continue
        ls_loc.append(a)
    if ls_loc:
        left_click(ls_loc[0])
    else:
        return False
    return True

def find_picture(lst:list,region=(50,50,400,400)):
    ls_loc=[]  
    for x in lst:  
        try:
            a=py.locateOnScreen(os.path.join(picture_folder,x),region=region, confidence=0.95)
        except:
            continue
        ls_loc.append(a)
        print(ls_loc)    

    return True if ls_loc else False


def trans_nc_explorer(machine):
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()
    path = r"C:\Users\Public\Desktop\NC Explorer"
    path = os.path.realpath(path)
    os.startfile(path)
    py_log.info('open nc Exp')
    sleep(5)
    if find_picture(('kolonki.png','kolonki1.png'),region=(1800,900,1920,1050))==False:
        keyboard.press_and_release('win + up')
        py_log.info('колонки не нашли win+up')

    if machine!='Nomura NN-20J3XB80(6)':
        a=os.path.join(picture_folder, 'subnet.png')
        py_log.info('open subnet')
        double_click(py.locateOnScreen(a,region=(100,100,400,400), confidence=0.5))
        # left_click((719, 400))
    lst=[(TFM_settings.picture(machine.strip())),
            ('cnc_mem1.png','cnc_mem2.png','cnc_mem3.png','cnc_mem4.png','cnc_mem5.png','cnc_mem6.png'),
        ('prg1.png','prg2.png','prg3.png','prg4.png'),
            ('user1.png','user2.png','user3.png','user4.png'),
    ]

    for x in lst:
        py_log.info('open '+x[0])
        double(x)
    sleep(10)
    
    if find_picture(['imya.png',])==False:
        py_log.info('если имени нет ищем колонки')
        for x in ('kolonki.png','kolonki1.png'):
            try:
                a=py.locateOnScreen(os.path.join(picture_folder,x),region=(1800,900,1920,1050), confidence=0.95)
            except:
                continue
        py_log.info('find kolonki')
        left_click(a)
    else:
        py_log.info('vidim kolonki')

    if find_picture(['galka.png',],region=(695,120,750,150))==False:
        py_log.info('нет даты правильной')                  
        a=py.locateOnScreen(os.path.join(picture_folder,'data.png'),region=(600,100,800,200), confidence=0.95)
        left_click(a)
    else:
        py_log.info('galka est')
    py.leftClick(234, 172,duration=0.25)  # первая программа
    sleep(1)
    keyboard.press('shift')
    sleep(1)
    py.moveTo(234, 518,duration=0.25)
    py.leftClick(234, 518)  # последняя программа
    keyboard.release('shift')
    sleep(1)
    keyboard.press_and_release('ctrl + c')
    sleep(1)
    os.startfile(os.path.join(TFM_settings.config.get_set_default('source'),machine))
    sleep(3)
    if find_picture(('folder_user.png',),region=(0,0,150,20))==True:
        keyboard.press_and_release('win + up')
        py_log.info('шапки папки нет win+up')
    sleep(3)
    keyboard.press_and_release('ctrl + v')
    sleep(3)
    if find_picture(('konflicti.png',),region=(730,690,820,750))==True:
        a=py.locateOnScreen(os.path.join(picture_folder,'konflicti.png'),region=(730,690,820,750), confidence=0.95)
        left_click(a)
        a=py.locateOnScreen(os.path.join(picture_folder,'kopir_zamena.png'),region=(730,350,950,430), confidence=0.95)
        left_click(a)
    py_log.info('галка конфликты')
    sleep(1)
    py.leftClick(860, 462,duration=0.25)
    sleep(10)
    left_click(py.locateOnScreen(os.path.join(picture_folder,'vihod.png'),region=(1868,0,1915,40), confidence=0.95))
    left_click(py.locateOnScreen(os.path.join(picture_folder,'vihod1.png'),region=(1868,0,1915,40), confidence=0.95))
    sleep(2)






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