import os

def file_search(path):  # ищем файл в папке  со станков
    for adress, dirs, files in os.walk(path):
        for file in files:
            adress_file_in_check = os.path.join(adress, file)
            yield adress_file_in_check  # возвращаем адрес файла

def mk_folder(path):
    if os.path.isdir(path)== False:
        os.makedirs(path)