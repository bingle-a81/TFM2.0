import os,yaml
import time
# ---------------
from logging_settings import set_logger
from TFM_settings import config
from working_file import ProgFile
from pprint import pprint

json_logger=set_logger('json_logger')

path=os.path.realpath(config.get_set_default('source')+config.get_set_default('DIR_TEMP')+config.get_set_default('YAML_FILE'))
path_for_base=os.path.realpath(config.get_set_default('DIR_FOR_BASE_UP'))


def serch_in_check(path_for_check):  # ищем файл в папке  со станков
    for adress, dirs, files in os.walk(path_for_check):
        for file in files:
            adress_file_in_check = os.path.join(adress, file)
            yield adress_file_in_check  # возвращаем адрес файла

def make_yaml_file():
    dict_programms={}
    for file in serch_in_check(path_for_base):
        if any(file.endswith(a) for a in
                ['mtx','xml','txt','jpg', 'pdf', 'bin', 'PDF', 'doc', 'zip', 'lnk', 'exe', 'db', 'docx', 'png', 'bmp', 'ICO', 'bat', '0L',
                '0C', 'gif', 'GIF','bmp','vbs','css','dtd','htm','htm','pptx','iso','sfv','prt','x_b','STEP','ipt','cdd','djvu',
                '__meta__','xlsx','PNG','tcl','dll','frw','bak','out','cdw','log','m3d','tif','rar','xls','spw','JPG','7z']) != True:
            programma=ProgFile(file)
            list_prog=list([programma.get_name_file_program(),programma.find_hash()])
            try:
                name_prog=programma.find_name_prog()
            except Exception as f:
                json_logger.debug(str(f)+'|'+file)
            if  dict_programms.get(name_prog,False)!=False:
                if  dict_programms.get(name_prog).get('adress')!=programma.find_folder():
                    json_logger.debug(file+'|'+programma.get_name_file_program())
                    continue
            dict_programms.setdefault(name_prog,{})
            dict_programms[name_prog]={'adress':programma.find_folder(),
                                        'prog':dict_programms[name_prog].get('prog',[])+[list_prog]}
            
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(dict_programms,f)


make_yaml_file()
   


d1={}
with open(path,'r',encoding='utf-8') as f:
    d1=yaml.load(f,Loader=yaml.FullLoader)

# a=d1.get('FAS4-A25-11-1').get('prog')[1][1]
# pprint(d1)
# print(a)

# quit(-1)


