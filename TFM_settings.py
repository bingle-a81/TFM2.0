from configparser import ConfigParser
import os

base_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_path, "set.ini")
# проверка наличия файла настоек
if os.path.exists(config_path):
    cfg = ConfigParser()
    cfg.read(config_path, encoding='utf-8')
else:
    print("Конфигурация не найдена!")


SERVER = cfg.get("smtp", "server")
PORT = cfg.get("smtp", "port")
EMAIL = cfg.get("smtp", "email")
PASSWD = cfg.get("smtp", "passwd")

TO_ADDR_MAIL = cfg.get("start", "TO_ADDR_MAIL")
PATH_FOR_CHECK = cfg.get("start", "PATH_FOR_CHECK")  # папка проги со станков
PATH_FOR_BASE = cfg.get("start", "PATH_FOR_BASE")  # папка УП/УП
PATH_FOR_COPY_NEW_FILES = cfg.get("start", "PATH_FOR_COPY_NEW_FILES")  # копируем новые файлы
ARCHIVE_PROGRAMM = cfg.get("start", "ARCHIVE_PROGRAMM")
LOG_FILE = cfg.get("start", "LOG_FILE")
LOG_FILE_DEBUG = cfg.get("start", "LOG_FILE_DEBUG")
SOURCE = cfg.get("start", "source")

CHAT_ID=cfg.get("telega", "chat_id")
TOKEN=cfg.get("telega", "token")

for each_section in cfg.sections('mashins'):
    for (each_key, each_val) in cfg.items(each_section):
        print (f'{each_key.upper()}:{each_val}')

# for x in cfg.get('mashins'):
#     print(x)

# nom=cfg.get('mashins','NomuraNN-20J2(1,2,3)')

# print(nom.split(';'))