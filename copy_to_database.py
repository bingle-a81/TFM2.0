import os,yaml
# --------------------
import simpe_functions
from TFM_settings import config
from working_file import ProgFile

path=config.get_yaml_file()

def start(machine):
    quantity_old = 0  # счетчики
    quantity_change = 0
    quantity_new = 0
    folder_mashine_tmp=os.path.join(config.get_set_default('source'),config.get_set_default('DIR_TEMP'),machine)
    dict_programms={}
    with open(path,'r',encoding='utf-8') as f:
        dict_programms=yaml.load(f,Loader=yaml.FullLoader)

    for file in simpe_functions.file_search(folder_mashine_tmp):  # ищем файл в папке  со станков
        programma=ProgFile(file)
        name_file_from_masine=programma.get_name_file_program()
        if name_file_from_masine in dict_programms:  # если имя файла есть в json-файле - то путь берем оттуда
            # path_for_base = dict_programms.get(name_file_from_masine).get('adress')
            TODO-----------
        else:
            path_for_base=os.path.realpath(config.get_set_default('DIR_FOR_BASE_UP'))

        for f in simpe_functions.file_search_in_base(path_for_base, name_file_from_masine):  # ищем файл в базе программ
            name_prog_old = find_name_prog(f)  # парсер названия
            if name_prog_old == name_prog:
                file_name_old = f
                logger.debug(f'добовляем в список {file_name_old}')
                lst.append(file_name_old)  # добовляем в список
                logger.debug(f'cсписок-- {lst}')
            else:
                continue
        logger.debug(f'общий список {lst}')
        # print(len(lst))
        name_of_machine = find_name_machine(folder_machine, file)  # парсер станка
        logger.debug(f'парсер станка {name_of_machine}')
        # logger.error(f'machine={name_of_machine}')

        if lst == []:  # если список пустой то файл новый-копируем в папку для новых файлов
            try:
                date_of_change = time.strftime('%d.%m.%Y', time.gmtime(attrib(file).date_of_change))
                logger.debug(f'date_of_change {date_of_change}')
                if os.path.isdir(
                        os.path.join(set.PATH_FOR_COPY_NEW_FILES, name_prog, name_of_machine, date_of_change)) == False:
                    os.makedirs(os.path.join(set.PATH_FOR_COPY_NEW_FILES, name_prog, name_of_machine, date_of_change))
                shutil.copyfile(file, os.path.join(set.PATH_FOR_COPY_NEW_FILES, name_prog, name_of_machine, date_of_change,
                                                   file_name_new))
                if os.path.isdir(os.path.join(set.ARCHIVE_PROGRAMM, name_prog, name_of_machine)) == False:
                    os.makedirs(os.path.join(set.ARCHIVE_PROGRAMM, name_prog, name_of_machine))
                shutil.copyfile(file, os.path.join(set.ARCHIVE_PROGRAMM, name_prog, name_of_machine, file_name_new))
                quantity_new += 1
                logger.info(f'file {name_prog} is new!!')

            except:
                logger.exception(f'Exception here, item = {name_prog}')
                logger1.exception(f'Exception here, item = {name_prog}')
                pass
        else:
            flag = all(attrib(i).size_file != attrib(file).size_file for i in lst)  # проверка - изменился ли размер файлов в списке
            logger.debug(f'проверка - изменился ли размер файлов в списке {flag} ')
            # logger.error(f'flag={flag}')
            if flag:  # новая версия старой программы
                try:
                    logger.debug(f'новая версия старой программы {flag} ')
                    dir_file_old = '\\'.join(file_name_old.split(('\\'))[0:10])  # путь до папки в БД УП
                    # logger.info(f'dir {dir_file_old}')
                    date_of_change = time.strftime('%d.%m.%Y', time.gmtime(attrib(file).date_of_change))
                    if os.path.isdir(os.path.join(dir_file_old, name_of_machine, date_of_change)) == False:
                        os.makedirs(os.path.join(dir_file_old, name_of_machine, date_of_change))
                    shutil.copyfile(file, os.path.join(dir_file_old, name_of_machine, date_of_change, file_name_new))

                    if os.path.isdir(os.path.join(set.ARCHIVE_PROGRAMM, name_prog, name_of_machine)) == False:
                        os.makedirs(os.path.join(set.ARCHIVE_PROGRAMM, name_prog, name_of_machine))
                    shutil.copyfile(file, os.path.join(set.ARCHIVE_PROGRAMM, name_prog, name_of_machine, file_name_new))

                    dir_file_old1 = '\\'.join(file_name_old.split(('\\'))[8:10])
                    quantity_change += 1
                    logger.debug(f'file {name_prog} copied to //{os.path.join(dir_file_old1, name_of_machine, date_of_change, file_name_new)}')
                    logger.info(
                        f'file {name_prog} copied to //{dir_file_old}')
                except:
                    logger.exception(f'Exception here ')
                    logger1.exception(f'Exception here, item = {name_prog}')
                    pass
            else:  # такая программа уже есть
                logger.debug(f'такая программа уже есть')
                quantity_old += 1
                logger.debug(f'file {name_prog} is {file_name_old}!Dont copy!')
                if os.path.isdir(os.path.join(set.ARCHIVE_PROGRAMM, name_prog, name_of_machine)) == False:
                    os.makedirs(os.path.join(set.ARCHIVE_PROGRAMM, name_prog, name_of_machine))
                shutil.copyfile(file, os.path.join(set.ARCHIVE_PROGRAMM, name_prog, name_of_machine, file_name_new))


    # --------------------------------------------------------------
