import os,yaml
import time
import pprint
# ---------------
from logging_settings import set_logger
from TFM_settings import config
from working_file import ProgFile
import simpe_functions

json_logger=set_logger('json_logger')

path=config.get_yaml_file()
path_for_base=os.path.realpath(config.get_set_default('DIR_FOR_BASE_UP'))

def make_yaml_file():
    dict_programms={}
    for file in simpe_functions.file_search(path_for_base):
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
                if  dict_programms.get(name_prog).get('adress')!=os.path.join(programma.find_zavod(),programma.find_folder()):
                    json_logger.debug(file+'|'+programma.get_name_file_program())
                    continue
            dict_programms.setdefault(name_prog,{})
            dict_programms[name_prog]={'adress':os.path.join(programma.find_zavod(),programma.find_folder()),
                                        'prog':dict_programms[name_prog].get('prog',[])+[list_prog]}
            
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(dict_programms,f)

def open_yaml_file(path):
    with open(path,'r',encoding='utf-8') as f:
        return yaml.load(f,Loader=yaml.FullLoader)    


# make_yaml_file()
   
if __name__ == '__main__':

    d1={}
    with open(path,'r',encoding='utf-8') as f:
        d1=yaml.load(f,Loader=yaml.FullLoader)

    pprint.pprint(d1)



# a=d1.get('FAS4-A25-11-1').get('prog')[1][1]
# pprint(d1)
# print(a)

# quit(-1)


