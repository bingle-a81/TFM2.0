
import os
# --------------
import make_yaml
from logging_settings import set_logger
from TFM_settings import config
import join_and_transfert_tmp
import copy_to_database
import pyauto

def yaml_start():
    make_yaml.make_yaml_file()

def pyauto_start_nomura(dc):    
    for x in dc.values():
        for y in x:
            pyauto.trans_nc_explorer(y)

def pyauto_start_fanuc(dc):    
    for x in dc.values():
        for y in x:
            pyauto.program_transfer_tool(y)

def pyauto_start_citizen(dc):    
    for x in dc.values():
        for y in x:
            pyauto.transfer_sitizen(y)            

def join_and_transfert_tmp_start_nomura(dc):    
    for x in dc.values():
        for y in x:
            join_and_transfert_tmp.common_files_nomura(y)

def join_and_transfert_tmp_start_other(dc):
    for x in dc.values():
        for y in x:
            join_and_transfert_tmp.trans_other_machine(y)    

def copy_to_database_start(dc):
    ls=[]
    for x in dc.values():
        ls+=x
    for x in ls:
       copy_to_database.trans(x)


# a_log=set_logger('simple_logger')



def start():
    dict_nomura=config.get_dict_section('NCExplorer') 
    dict_fanuc=config.get_dict_section('PttMain')   
    dict_citizen=config.get_dict_section('FileControl')
    dict_other=config.get_dict_section('other')
    dict_all={**dict_nomura,**dict_fanuc,**dict_citizen,**dict_other}



    # yaml_start()       
    # # quit(-1)

    # pyauto_start_nomura(dict_nomura)
    pyauto_start_citizen(dict_citizen)

    # join_and_transfert_tmp_start_nomura(dict_nomura)
    # join_and_transfert_tmp_start_other(dict_fanuc)
    # join_and_transfert_tmp_start_other(dict_citizen)   
    # join_and_transfert_tmp_start_other(dict_other)

    # copy_to_database_start(dict_all)

            


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