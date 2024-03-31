import os,yaml
import time
from logging_settings import set_logger
from TFM_settings import config
import re




path=os.path.realpath(config.get_set_default('source')+config.get_set_default('DIR_TEMP')+config.get_set_default('YAML_FILE'))
path_for_base=os.path.realpath(config.get_set_default('DIR_FOR_BASE_UP'))

d={}
def serch_in_check(path_for_check):  # ищем файл в папке  со станков
    for adress, dirs, files in os.walk(path_for_check):
        for file in files:
            adress_file_in_check = os.path.join(adress, file)
            yield adress_file_in_check  # возвращаем адрес файла

for i in serch_in_check(path_for_base):
    r=i.split('\\')
    d.setdefault(r[7],[]).append(r[-1])

print(d)
   
quit(-1)
def correction_of_the_line(string):  # удаляем символы кроме букв,цифр и точки
    reg = re.compile('[^a-zA-Z0-9. -]')
    a = reg.sub('', string)
    a=a.strip()
    a=a.rstrip('.')
    return a


def find_name_prog(path):  # из программы извлекаем имя файла в скобках
    with open(path, 'r') as r:  # только чтение файла
        i = 0
        while i < 3:
            st = r.readline()  # чтение текстового файла построчно
            i += 1
            if ('(' in st) and (')' in st):
                f_name = st[(st.index('(') + 1):(st.index(')'))].strip()
                f_name = correction_of_the_line(f_name).strip()
                # logger.debug(f'name++{f_name}')
                return f_name
                break
            else:
                pass
        else:
            a = chenge_name(path.split('\\')[-1])  # если в файле названия нет - берем имя файла
            return chenge_name(path.split('\\')[-1])
        
def serch_in_check(path_for_check):  # ищем файл в папке  со станков
    for adress, dirs, files in os.walk(path_for_check):
        for file in files:
            adress_file_in_check = os.path.join(adress, file)
            yield adress_file_in_check  # возвращаем адрес файла

def chenge_name(st=''):  # удаляем расширение файла
    if st.rfind('.') > 0:
        return st[0:st.rfind('.')]
    else:
        return st



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