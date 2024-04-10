import os,shutil

def file_search(path):  # ищем файл в папке  со станков
    for adress, dirs, files in os.walk(path):
        for file in files:
            adress_file_in_check = os.path.join(adress, file)
            yield adress_file_in_check  # возвращаем адрес файла

def mk_folder(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    # if os.path.isdir(path)== True:
    #     shutil.rmtree(path, ignore_errors=True)
    # os.makedirs(path)

        

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