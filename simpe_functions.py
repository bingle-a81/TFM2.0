import os,shutil

def file_search(path):  # ищем файл в папке  со станков
    for adress, dirs, files in os.walk(path):
        for file in files:
            adress_file_in_check = os.path.join(adress, file)
            yield adress_file_in_check  # возвращаем адрес файла

def mk_folder(path):
    if os.path.isdir(path)== False:
        os.makedirs(path)

def file_search_in_base(path,file_name):
    try:
        for adress, dirs, files in os.walk(path):
            for file in files:
                if file == file_name:
                    adress_file_in_base = os.path.join(adress, file)
                    yield adress_file_in_base  # возвращаем адрес файла
    except Exception as ex:
       print(ex)  

def copy_file(path_folder_kuda,path_folder_otkuda):
    a=path_folder_otkuda.split('\\')[-1]
    if os.path.isdir(path_folder_kuda) == False:
        os.makedirs(path_folder_kuda)
    shutil.copyfile(path_folder_otkuda,os.path.join(path_folder_kuda,a))    