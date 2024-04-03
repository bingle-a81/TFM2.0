import os
# --------------------
import simpe_functions
from TFM_settings import config
from working_file import ProgFile
import make_yaml
# TODO(логгирование)

# path=config.get_yaml_file()

def start(machine):
    quantity_old = 0  # счетчики
    quantity_change = 0
    quantity_new = 0
    source=config.get_set_default('source')
    new_source=source+config.get_set_default('PATH_FOR_COPY_NEW_FILES')
    up_source=config.get_set_default('DIR_FOR_BASE_UP')
    folder_machine_tmp=os.path.join(source,config.get_set_default('DIR_TEMP'),machine)

    dict_programms=make_yaml.open_yaml_file(config.get_yaml_file())
    for file in simpe_functions.file_search(folder_machine_tmp):  # ищем файл в папке  со станков
        programma=ProgFile(file)     
        name_file_from_machine=programma.find_name_prog()
        if name_file_from_machine in dict_programms:  # если имя файла есть в yaml-файле - то путь берем оттуда
            lst=dict_programms.get(name_file_from_machine).get('prog')
            for x in lst:
                if programma.find_hash()==x[1]:                        
                        print(name_file_from_machine,f'({x[0]})','=find it:',programma.find_hash(),'--',x[1])
                        break
            else:
                # TODO(запись в базу уп)                
                copy_f(programma,machine,dict_programms.get(name_file_from_machine).get('adress'),up_source)     
            
        else:
            # up_source=source+config.get_set_default('PATH_FOR_COPY_NEW_FILES')
            copy_f(programma,machine, programma.find_name_prog(),new_source)


def copy_f(programma:ProgFile,mashine:str,progr_folder:str,up_source):
    data_of_change=programma.get_date_of_change()    
    arhiv_source=config.get_set_default('ARCHIVE_PROGRAMM')
    path_progr=os.path.join(up_source, progr_folder,mashine,data_of_change)
    path_arhive_progr=os.path.join(arhiv_source, programma.find_name_prog(),mashine)
    simpe_functions.copy_file(path_progr,programma.get_path())
    simpe_functions.copy_file(path_arhive_progr,programma.get_path())
     



# start('None')