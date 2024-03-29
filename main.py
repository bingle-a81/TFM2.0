import  AppOpener
import os
def start():
    # AppOpener.open("roll_up")

    path = r"C:\Users\Public\Desktop\NC Explorer"
    path = os.path.realpath(path)
    os.startfile(path)


# -----------------------------------------------------------------------
if __name__ == '__main__':
    start()