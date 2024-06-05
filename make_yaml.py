import os, yaml
import time

# ---------------
from logging_settings import set_logger
from TFM_settings import config
from working_file import ProgFile
import simpe_functions


def make_yaml_file():
    count_mistake_file = 0
    programs_with_error = set()

    yaml_logger = set_logger("yaml_logger")

    path = config.get_yaml_file("YAML_FILE")
    path_yaml_error = config.get_yaml_file("YAML_FILE_ERROR")
    path_for_base = os.path.realpath(config.get_set_default("DIR_FOR_BASE_UP"))
    dict_programms = {}
    for file in simpe_functions.file_search(path_for_base):
        if (
            any(
                file.endswith(a)
                for a in [
                    "mtx",
                    "xml",
                    "txt",
                    "jpg",
                    "pdf",
                    "bin",
                    "PDF",
                    "doc",
                    "zip",
                    "lnk",
                    "exe",
                    "db",
                    "docx",
                    "png",
                    "bmp",
                    "ICO",
                    "bat",
                    "0L",
                    "0C",
                    "gif",
                    "GIF",
                    "bmp",
                    "vbs",
                    "css",
                    "dtd",
                    "htm",
                    "htm",
                    "pptx",
                    "iso",
                    "sfv",
                    "prt",
                    "x_b",
                    "STEP",
                    "ipt",
                    "cdd",
                    "djvu",
                    "__meta__",
                    "xlsx",
                    "PNG",
                    "tcl",
                    "dll",
                    "frw",
                    "bak",
                    "out",
                    "cdw",
                    "log",
                    "m3d",
                    "tif",
                    "rar",
                    "xls",
                    "spw",
                    "JPG",
                    "7z",
                    "ptp",
                ]
            )
            != True
        ):
            programma = ProgFile(file)
            list_prog = list([programma.get_name_file_program(), programma.find_hash()])
            try:
                name_prog = programma.find_name_prog()
            except Exception as f:
                yaml_logger.info(str(f) + "|" + file)
                count_mistake_file += 1
                # programs_with_error.add(programma.get_name_file_program())
            if dict_programms.get(name_prog, False) != False:
                if dict_programms.get(name_prog).get("adress") != os.path.join(
                    programma.find_zavod(), programma.find_folder()
                ):
                    yaml_logger.info(
                        dict_programms.get(name_prog).get("adress")
                        + "="
                        + file
                        + "|"
                        + programma.get_name_file_program()
                    )
                    count_mistake_file += 1
                    programs_with_error.add(name_prog)
                    continue
            dict_programms.setdefault(name_prog, {})
            dict_programms[name_prog] = {
                "adress": os.path.join(programma.find_zavod(), programma.find_folder()),
                "prog": dict_programms[name_prog].get("prog", []) + [list_prog],
            }

    yaml_logger.warning(f"кол-во файлов не в своих папках {count_mistake_file}")
    time.sleep(5)
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(dict_programms, f)

    with open(path_yaml_error, "w", encoding="utf-8") as f:
        yaml.safe_dump(programs_with_error, f)


def open_yaml_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)
