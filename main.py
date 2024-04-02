import  AppOpener
import os
from logging_settings import set_logger


a_log=set_logger('simple_logger')



def start():
    pass

    # try:
    #     print(5/0)
    # except ZeroDivisionError as f:
    #     a_log.info(f)

# def start():
#     # AppOpener.open("roll_up")

#     path = r"C:\Users\Public\Desktop\NC Explorer"
#     path = os.path.realpath(path)
#     os.startfile(path)


# -----------------------------------------------------------------------
if __name__ == '__main__':
    start()