import pyautogui as py
import os
from time import sleep
import keyboard
# -----------
from logging_settings import set_logger



class MachinePyautogui:
    def __init__(self) -> None:
        # self._name=name
        self._log=set_logger('py_logger')
        self.__picture_folder=r'.picture\\nomura\\'
        self.__othod=(1300, 400)

    @staticmethod
    def format_point(point):
        return '('+','.join(str(x) for x in point)+')'

    def left_double_click(self,point):
        py.moveTo(point)
        py.doubleClick(point,button='LEFT',duration=0.25)
        self._log.info('дважды нажата кнопка: '+self.format_point(point))


    def left_click(self,point,):
        py.moveTo(point, duration=0.25)
        py.leftClick(point, duration=0.25) 
        if point==self.__othod:
            self._log.info('мышь отход') 
            return        
        self._log.info('один раз нажата кнопка: '+self.format_point(point))  

    def open_pic_folder(self,lst:list,region=(50,50,400,400),click=2):
        for x in lst:            
            sleep(1)
            path=os.path.join(self.__picture_folder,x)
            try:
                a=py.locateOnScreen(path,region=region, confidence=0.95)
            except:
                continue                            
            sleep(1)
            if a:
                self._log.info('найден '+x)  
                match click:
                    case 1:
                        self.left_click(a)
                    case 2:
                        self.left_double_click(a)
                    case '_':
                        print('mistake')
                self.left_click(self.__othod)
                return True
        self._log.info('pic не найдены '+self.format_point(lst))  
        return False
    
    def find_picture(self,lst:list,region=(50,50,400,400)):
        for x in lst: 
            sleep(1)
            path=os.path.join(self.__picture_folder,x) 
            try:
                a=py.locateOnScreen(path,region=region, confidence=0.95)
            except:
                continue
            sleep(1)
            if a :
                self._log.info('найден '+x)  
                return True 
        self._log.info('pic не найдены '+self.format_point(lst))  
        return False
            
    def hotkey(self,hot:str):        
        keyboard.press(hot)
        sleep(0.5)
        keyboard.release(hot)
        self._log.info('нажаты кнопки '+hot)  

    def open_folder_os(self,path):
        path = os.path.realpath(path)
        os.startfile(path)
        self._log.info('открыта папка '+ path)  