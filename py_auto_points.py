import os
from time import sleep
import AppOpener
# ?----------------
from logging_settings import set_logger
import TFM_settings
from py_functions import MachinePyautogui

def py_citizen_points():
    foo=MachinePyautogui('citizen',r'.picture\\citizen\\')
    AppOpener.open("filecontrol") 
    
    lst=((1211,326,17,19),(1073,346,56,13),(701,274,34,22),(723,331),(895,323,59,28),(987,475,36,18),(943,642,87,30),(970,656,81,55),(978,555,76,24),(864,597,105,23))
    lst2=((1211,326,17,19),(1074,357,54,14),(701,274,34,22),(723,331),(895,323,59,28),(987,493,36,18),(943,642,87,30),(970,656,81,55),(978,555,76,24),(864,597,105,23))
    

    for x in lst:
        foo.left_click(x)
        sleep(2)
    sleep(25)
    for x in lst2:
        foo.left_click(x)
        sleep(1)    
    sleep(25)
    foo.left_click((1170,727,71,43))




if __name__ == '__main__':
    py_citizen_points()

