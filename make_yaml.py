import os,yaml
import time
from logging_settings import set_logger
from TFM_settings import config

a=config.get_set_default('source')+config.get_set_default('DIR_TEMP')+config.get_set_default('YAML_FILE')
path=os.path.realpath(a)

path_for_base=config.get_set_default('DIR_FOR_BASE_UP')

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

print(len(data))

var_dict={}
from itertools import product
N=363
M=500
K=2
for (i,j,k) in product(range(N),range(M),range(K)):
    var_name='x_'+'_'+str(i)+str(j)+'_'+str(k)
    var_dict[var_name] = var_name
print (len(var_dict))

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