import  AppOpener
import os
# --------------
import make_yaml
from logging_settings import set_logger
from TFM_settings import config
import join_and_transfert_tmp
import copy_to_database



a_log=set_logger('simple_logger')



def start():
    make_yaml.make_yaml_file()
    lst1=config.get_dict_section('NCExplorer')
    for x in lst1.values():
        for y in x:
            join_and_transfert_tmp.common_files_nomura(y)
    lst2={**config.get_dict_section('PttMain'),**config.get_dict_section('FileControl'),**config.get_dict_section('other')}
    for x in lst2.values():
        for y in x:
            join_and_transfert_tmp.trans_other_machine(y)

    lst3={**lst1,**lst2}
    # ls=[x for x in lst3.values()]
    ls=[]
    for x in lst3.values():
        ls+=x
    for x in ls:
       copy_to_database.trans(x)

            


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