from configparser import ConfigParser
import os

def picture(machine):
    match machine:
        case 'Nomura NN-20J2(1)':
            return ('nom1.png','nom11.png')
        case 'Nomura NN-20J2(2)':
            return ('nom2.png','nom22.png')
        case 'Nomura NN-20J2(3)':
            return ('nom3.png','nom33.png')      
        case 'Nomura NN-20J3(4)':
            return ('nom4.png','nom44.png')    
        case 'Nomura NN-20J3(5)':
            return ('nom5.png','nom55.png')         
        case 'Nomura NN-20J3XB80(6)':
            return ('nom6.png','nom66.png')            
        case 'Nomura NN-10E':
            return ('nom10.png','nom110.png')     
        case 'Nexturn SA-26PY':
            return ('next261.png',)                   
        case 'Miyano BNJ-42SY':
            return ('miano.png',)    
        case 'Hanhwa XD20H':
            return ('hanva.png',)   
        case 'Colchester T8MSY':
            return ('colchester.png',)              
        case 'Nexturn SA-12B(1)':
            return ('next1.png',)    
        case 'Nexturn SA-12B(2)':
            return ('nex2.png',)       
        case 'Tsugami SS267-III':
            return ('tsug267.png',)    
        case 'Tsugami M08SY-II':
            return ('tsu08.png',)                      
        case 'Tsugami BO126TF-III':
            return ('ts126.png',)   
        case 'Citizen Cincom L12(1)':
            return ('citizen_machine1.png','citizen_folder1.png','citizen_folder11.png')           
        case 'Citizen Cincom L12(2)':
            return ('citizen_machine2.png','citizen_folder2.png','citizen_folder22.png')          
        case '_'                              :
            print('нет такого станка')

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
