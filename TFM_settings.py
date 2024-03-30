from configparser import ConfigParser
import os

class Get_config():
    def __init__(self,name_file) -> None:
        self._name=name_file
        self.init()

    def init(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_path,self._name)
        if os.path.exists(config_path):
            self.cfg = ConfigParser()
            self.cfg.optionxform=str
            self.cfg.read(config_path, encoding='utf-8')
        else:
            print("Конфигурация не найдена!")
            quit(-1)

    def get_set(self,section,option):
        return self.cfg.get(section, option)
    
    def get_set_default(self,option):
        return self.cfg.get('default', option)    

    def get_dict_section(self,section):
        return {k:v.split(';') for k,v in self.cfg[section].items()}

        # for key, val in cfg['NCExplorer'].items():
#     d=key
#     print (f'{d}:{val.split(';')}')




config=Get_config('set.ini')
# print(a.get_set_default('source'))
# print(a.get_dict_section('NCExplorer'))
    


# проверка наличия файла настоек


# a=cfg.get('default','MAIN_PATH')
# b=cfg.get('default','PATH_FOR_CHECK')
# path = os.path.realpath(a+b)
# os.chdir(path)
# os.mkdir('11')
# print(a)


# SERVER = cfg.get("smtp", "server")
# PORT = cfg.get("smtp", "port")
# EMAIL = cfg.get("smtp", "email")
# PASSWD = cfg.get("smtp", "passwd")

# TO_ADDR_MAIL = cfg.get("start", "TO_ADDR_MAIL")
# PATH_FOR_CHECK = cfg.get("start", "PATH_FOR_CHECK")  # папка проги со станков
# PATH_FOR_BASE = cfg.get("start", "PATH_FOR_BASE")  # папка УП/УП
# PATH_FOR_COPY_NEW_FILES = cfg.get("start", "PATH_FOR_COPY_NEW_FILES")  # копируем новые файлы
# ARCHIVE_PROGRAMM = cfg.get("start", "ARCHIVE_PROGRAMM")
# LOG_FILE = cfg.get("start", "LOG_FILE")
# LOG_FILE_DEBUG = cfg.get("start", "LOG_FILE_DEBUG")
# SOURCE = cfg.get("start", "source")

# CHAT_ID=cfg.get("telega", "chat_id")
# TOKEN=cfg.get("telega", "token")
# a=[]


# for key, val in cfg['NCExplorer'].items():
#     d=key
#     print (f'{d}:{val.split(';')}')
    
# for key in cfg['PttMain'].keys():
#     print (key)

# d={'FG':1,'HJ':2}
# print(d.keys())


    # for (each_key, each_val) in cfg.items(each_section):
    #     print (f'{each_key.capitalize()}:{each_val}')

# for x in cfg.get('mashins'):
#     print(x)

# nom=cfg.get('mashins','NomuraNN-20J2(1,2,3)')

# print(nom.split(';'))