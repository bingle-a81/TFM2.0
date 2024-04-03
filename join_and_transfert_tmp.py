import os, shutil, time
from logging_settings import set_logger
from TFM_settings import config
import simpe_functions

   

def common_files_nomura(machine):
    folder_mashine_tmp=os.path.join(config.get_set_default('source'),config.get_set_default('DIR_TEMP'),machine)
    folder_mashine=os.path.join(config.get_set_default('source'),machine)
    simpe_functions.mk_folder(folder_mashine_tmp)
    simpe_functions.mk_folder(folder_mashine)
    for file in simpe_functions.file_search(folder_mashine):  # ищем файл в папке  со станков
        file_name = file.split('\\')[-1]  # имя файла файла со станков
        if '$2' not in file_name:
            file_name_2='$2$'+file_name
            if os.path.exists(os.path.join(folder_mashine,file_name_2)):
                with open (os.path.join(folder_mashine,file_name),'r') as f1:
                    first_file=f1
                    with open (os.path.join(folder_mashine,file_name_2),'r') as f2: 
                        second_file=f2
                        with open (os.path.join(folder_mashine_tmp,file_name),'w') as f3: 
                            common_file=f3
                            a='\n$1\n'
                            for line in first_file:
                                if '%' not in line:
                                    a=a+line
                            common_file.write(a)
                            a='$2\n'
                            for line in second_file:
                                if '%' not in line:
                                    a=a+line
                                else:
                                    a=a+'%'
                            common_file.write(a)


def trans_other_machine(machine):
    folder_mashine_tmp=os.path.join(config.get_set_default('source'),config.get_set_default('DIR_TEMP'),machine)
    folder_mashine=os.path.join(config.get_set_default('source'),machine)
    simpe_functions.mk_folder(folder_mashine_tmp)
    simpe_functions.mk_folder(folder_mashine)

    for file in simpe_functions.file_search(folder_mashine):  # ищем файл в папке  со станков
        shutil.copy(file,os.path.join(os.path.join(folder_mashine_tmp)))  # клонируем папки в папку для разбора

        


# for x in lst:
#     print(x.items())
        # print(y)
# print(lst)
        

    # spisok = []
    # if os.path.isfile(os.path.join(path_for_check_join,machine+'-ignor.txt')):
    #     with open(os.path.join(path_for_check_join,machine+'-ignor.txt'),'r') as f:
    #         spisok=list(f.read().split(' '))        