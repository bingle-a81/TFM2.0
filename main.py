import os, time, shutil
import py_win_keyboard_layout

# --------------
import make_yaml
from logging_settings import set_logger
from TFM_settings import config
import join_and_transfert_tmp
import copy_to_database
import pyauto
import py_auto_points

main_logger = set_logger("telega_logger")


def update_folder(machine):
    aa = os.path.join(config.get_set_default("source"), machine)
    if os.path.isdir(aa) == True:
        shutil.rmtree(aa, ignore_errors=True)
    os.makedirs(aa)


def counter(foo):
    def wrapper(*args, **kwargs):
        start_count = time.perf_counter()
        main_logger.warning(f"начало {foo.__name__} \n")
        foo(*args, **kwargs)
        main_logger.warning(
            f'Время работы {foo.__name__} {time.strftime("%H:%M:%S", time.gmtime(time.perf_counter() - start_count))} \n'
        )
        return

    return wrapper


@counter
def yaml_start():
    make_yaml.make_yaml_file()
    time.sleep(5)


@counter
def pyauto_start_nomura(dc):
    for x in dc.values():
        for y in x:
            update_folder(y)
            pyauto.trans_nc_explorer(y)


@counter
def pyauto_start_fanuc(dc):
    for x in dc.values():
        for y in x:
            update_folder(y)
            pyauto.program_transfer_tool(y)


@counter
def pyauto_start_citizen(dc):
    for x in dc.values():
        for y in x:
            update_folder(y)
    py_auto_points.py_citizen_points()
    source = config.get_set_default("source")
    for x in dc.values():
        for y in x:
            folder_machine_tmp = os.path.join(source, y)
            q = len(
                [
                    name
                    for name in os.listdir(folder_machine_tmp)
                    if os.path.isfile(os.path.join(folder_machine_tmp, name))
                ]
            )
            if q == 0:
                pyauto.transfer_sitizen(y)


def join_and_transfert_tmp_start_nomura(dc):
    for x, y in dc.items():
        join_and_transfert_tmp.common_files_nomura(x, y)


def join_and_transfert_tmp_start_other(dc):
    for x, y in dc.items():
        join_and_transfert_tmp.trans_other_machine(x, y)


@counter
def copy_to_database_start(dc):
    for x in dc:
        copy_to_database.trans(x)


def change_keyboard_layout():
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)


@counter
def start():
    a = 5
    dict_nomura = config.get_dict_section("NCExplorer")
    dict_fanuc = config.get_dict_section("PttMain")
    dict_citizen = config.get_dict_section("FileControl")
    dict_other = config.get_dict_section("other")
    dict_all = {**dict_nomura, **dict_fanuc, **dict_citizen, **dict_other}

    # time.sleep(a)
    # yaml_start()
    # time.sleep(a)

    # change_keyboard_layout()
    # pyauto_start_citizen(dict_citizen)
    # time.sleep(a)
    pyauto_start_nomura(dict_nomura)
    time.sleep(a)
    pyauto_start_fanuc(dict_fanuc)
    time.sleep(a)

    join_and_transfert_tmp_start_nomura(dict_nomura)
    join_and_transfert_tmp_start_other(dict_fanuc)
    join_and_transfert_tmp_start_other(dict_citizen)
    join_and_transfert_tmp_start_other(dict_other)

    copy_to_database_start(dict_all)
    time.sleep(a)


# -----------------------------------------------------------------------
if __name__ == "__main__":
    start()

    email_logger = set_logger("email_logger")
    a = copy_to_database.file_name_base_logger
    with open(a, "r") as f:
        message = f.read()

    email_logger.warning(message)
