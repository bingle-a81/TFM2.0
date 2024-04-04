from configparser import ConfigParser
import os

def picture(machine):
    match machine:
        case 'Nomura NN-20J2(1)':
            return ('nom1.png','nom11.png')

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
        return {k:v.split('|') for k,v in self.cfg[section].items()}
    
    def get_yaml_file(self):
        return os.path.realpath(config.get_set_default('source')+config.get_set_default('DIR_TEMP')+config.get_set_default('YAML_FILE'))



config=Get_config('set.ini')
