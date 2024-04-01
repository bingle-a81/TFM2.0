import os,yaml
import time
from logging_settings import set_logger
from TFM_settings import config
from working_file import ProgFile
from pprint import pprint


path=os.path.realpath(config.get_set_default('source')+config.get_set_default('DIR_TEMP')+config.get_set_default('YAML_FILE'))
path_for_base=os.path.realpath(config.get_set_default('DIR_FOR_BASE_UP'))

d={}
def serch_in_check(path_for_check):  # ищем файл в папке  со станков
    for adress, dirs, files in os.walk(path_for_check):
        for file in files:
            adress_file_in_check = os.path.join(adress, file)
            yield adress_file_in_check  # возвращаем адрес файла

for i in serch_in_check(path_for_base):
    r=ProgFile(i)
    if d.get(r.find_name()):
        a=d.get(r.find_name())
        if  a[0][0]==r.find_folder():
            print('tt')

    d.setdefault(r.find_name(),[]).append([r.find_folder(),r.find_hash()])


   
with open(path, "w", encoding="utf-8") as f:
    yaml.dump(d,f)

d1={}
with open(path,'r',encoding='utf-8') as f:
    d1=yaml.load(f,Loader=yaml.FullLoader)

# pprint(d1)

quit(-1)




        
def serch_in_check(path_for_check):  # ищем файл в папке  со станков
    for adress, dirs, files in os.walk(path_for_check):
        for file in files:
            adress_file_in_check = os.path.join(adress, file)
            yield adress_file_in_check  # возвращаем адрес файла





with open(path, "w", encoding="utf-8") as f:        
    for file in serch_in_check(path_for_base):  #ищем файл в папке  со станков
        ff=file.split('\\')[-2]
        file_name_new = file.split('\\')[-1]  # имя файла файла со станков
        yaml.dump([{ff:file_name_new,}],f)

with open(path, "r", encoding="utf-8") as file:
    data=yaml.load(file,Loader=yaml.FullLoader)

print(data)


# for x in data:
#     for k,v in x.items():
#         print(v)



# Convert and print the JSON data in YAML stream
# print(yaml.dump(books))
# with open(path, "w+", encoding="utf-8") as file:
#     file.write(yaml.dump(books,indent=4))
# with open(path, "r", encoding="utf-8") as file:
#     data=yaml.load(file,Loader=yaml.FullLoader)

# for x in data:
#     if x['author']=='Luciano Ramalho':
#         print(x['price'])