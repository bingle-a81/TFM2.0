import os
from time import sleep
import keyboard
from ctypes import windll
import win32api
from subprocess import Popen, PIPE
import psutil
# -------------------
from logging_settings import set_logger
import TFM_settings
from py_functions import MachinePyautogui

# sleep=time.sleep(5)
py_log=set_logger('py_logger')

def sitizen(a,dict1):
    picture_link = r'c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\picture'
    for process in (process for process in psutil.process_iter() if process.name() == "FileControl.exe"):
        process.kill()
        sleep(4)

    os.startfile(r'C:\Program Files (x86)\FileControl\FileControl.exe')

    sleep(3)

    pyautogui.leftClick(1220, 340,duration=0.25)

    sleep(2)
    pyautogui.leftClick(dict1.get('machine'),duration=0.25)

    sleep(2)
    pyautogui.leftClick(943, 338,duration=0.25)

    sleep(2)
    for x in range(3):
        pyautogui.leftClick(1096, 599)
        logger.debug('клик вниз')
        sleep(1)
    pic_machine = next((item for item in list(
        map(lambda x: pyautogui.locateCenterOnScreen(x), dict1.get('pic_machine_lst'))) if item is not None), None)
    logger.debug(f'вывод = {pic_machine}')
    i=0
    while pic_machine==None:
        sleep(0.1)
        for x in  dict1.get('pic_machine_lst'):
            pic_machine=pyautogui.locateCenterOnScreen(x)
            if pic_machine!=None:
                break
            else:
                i += 1
                logger.debug(f'счетчик {i} pic2={pic_machine}')
        if i>10 :
            logger.debug(f'станок {a} не открывается')
            return
    pyautogui.moveTo(pic_machine)
    pyautogui.leftClick(pic_machine,duration=0.25)
    logger.debug(f'выбор папки {a}')
    pyautogui.leftClick(1002, 660,duration=0.25)
    logger.debug('кнопка ок')
    sleep(2)
    pyautogui.leftClick(717, 288,duration=0.25)
    logger.debug('edit')
    sleep(2)
    pyautogui.leftClick(767, 334,duration=0.25)
    logger.debug(f'select all on machine {a}')
    sleep(2)
    pyautogui.leftClick(999, 676,duration=0.25)
    logger.debug('transfer to pc')
    sleep(2)
    pyautogui.leftClick(1012, 572,duration=0.25)
    logger.debug('да')
    sleep(2)
    pyautogui.leftClick(927, 615,duration=0.25)
    logger.debug('хз')
    sleep(55)
    for process in (process for process in psutil.process_iter() if process.name() == "FileControl.exe"):
        process.kill()
    return True



def transfer_fanuc(foo):

    foo.left_click((306,350))  # первая программа
    sleep(1)
    keyboard.press('shift')
    sleep(1)
    foo.left_click((306, 420))  # последняя программа
    keyboard.release('shift')
    sleep(1)
    foo.right_click((306, 420))
    foo.open_pic_folder(('upload.png',),region=(250,410,800,600),click=1) 
    foo.open_pic_folder(('upl_button.png','upl_button1.png'),region=(290,400,650,650),click=1)
    sleep(5)
    if foo.find_picture(('yes_to_all.png',),region=(750,450,1200,660)):
        foo.open_pic_folder(('yes_to_all.png',),region=(750,550,1100,660),click=1) 
    foo.open_pic_folder(('uppl_but_ok.png','uppl_but_ok1.png'),region=(900,500,1200,680),click=1)  
    sleep(5) 


def program_transfer_tool(machine):
    p=r'.picture\\fanuc\\'
    foo=MachinePyautogui(machine,p)
    picture = r'c:\Users\Programmer\PycharmProjects\Transfer_From_Machine\picture\fanuc_last_mod.png'
    for process in (process for process in psutil.process_iter() if process.name() == "PttMain.exe"):
        process.kill()
    sleep(4)
    foo.open_folder_os(r'C:\Program Files (x86)\FANUC\Program Transfer Tool\Bin\PttMain.exe')
    sleep(6)
    foo.hotkey('win + up')#full screen
    sleep(2)
    if foo.find_picture(TFM_settings.picture(machine.strip()),region=(0,300,250,850)):
        foo.open_pic_folder(TFM_settings.picture(machine.strip()),region=(0,300,250,850),click=1) 
    else:
        foo.open_pic_folder(('vihod.png',),region=(1868,0,1915,40),click=1)
        return 
    sleep(10) 
    if foo.find_picture(('PTT_mess.png',),region=(750,450,1200,660)):
        foo.open_pic_folder(('knopka_fanuc_net_stanka.png',),region=(750,450,1200,660),click=1)
        for process in (process for process in psutil.process_iter() if process.name() == "PttMain.exe"):
            process.kill()
        return  
    # foo.open_pic_folder(('path1.png','path3.png','path5.png','path7.png'),region=(0,300,350,850),click=1)
    foo.open_pic_folder(('last_mod.png',),region=(851,310,1800,350),click=1) 
    transfer_fanuc(foo)

    if machine not in ('Colchester T8MSY','Tsugami M08SY-II'):
        foo.open_pic_folder(('path2.png','path4.png','path8.png'),region=(0,300,250,850),click=1)
        transfer_fanuc(foo)

    for process in (process for process in psutil.process_iter() if process.name() == "PttMain.exe"):
        process.kill()
    sleep(3)
    return True

   
def trans_nc_explorer(machine):
    p=r'.picture\\nomura\\'
    foo=MachinePyautogui(machine,p)

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

    if foo.find_picture(TFM_settings.picture(machine.strip())):
        foo.open_pic_folder(TFM_settings.picture(machine.strip()))  
    else:
        foo.open_pic_folder(('vihod.png',),region=(1868,0,1915,40),click=1)
        return  


    lst=[('cnc_mem1.png','cnc_mem2.png','cnc_mem3.png','cnc_mem4.png','cnc_mem5.png','cnc_mem6.png'),
        ('prg1.png','prg2.png','prg3.png','prg4.png'),
            ('user1.png','user2.png','user3.png','user4.png'), ]
    for x in lst:
        if foo.find_picture(x):
            foo.open_pic_folder(x)
        else:
            foo.open_pic_folder(('vihod.png',),region=(1868,0,1915,40),click=1)
            return              

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
    foo.open_pic_folder(('vihod1.png',),region=(1868,0,1915,40),click=1)
    py_log.info('программы скачаны')






if __name__ == '__main__':
    ls=TFM_settings.config.get_dict_section('NCExplorer')
    print(ls)
    # for x in (ls):
    #     trans_nc_explorer(x)
    

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

# a=r'.picture\Screenshot_1.png'
# if os.path.isfile(a):
#     print('jk')
#     a = os.path.realpath(a)
#     # os.startfile(a)
# a = os.path.realpath(a)
# print(a)
# b=py.locateOnScreen(a,region=(107,103,500,500), confidence=0.95)
# print(b)
# ,region=(170,200,270,300), confidence=0.95

# .locateOnScreen(x,region=(164,104,240,200), confidence=0.95)
# py.moveTo(b)
# print(py.position())

# keyboard.wait('space')
# print (win32api.GetCursorPos())