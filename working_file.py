import re
import hashlib
import time, os

# ------------
from TFM_settings import config


class ProgFile:
    def __init__(self, path) -> None:
        self._path = path

    def get_path(self):
        return self._path

    def get_name_file_program(self):
        return self._path.split("\\")[-1]

    def get_date_of_change(self):
        return time.strftime(
            "%d.%m.%Y", time.strptime(time.ctime(os.path.getmtime(self._path)))
        )

    def find_name_prog(self):
        # try:
        with open(self._path, "r", encoding="windows-1252") as r:  # только чтение файла
            i = 0
            while i < 3:
                st = r.readline()  # чтение текстового файла построчно
                i += 1
                if ("(" in st) and (")" in st):
                    f_name = st[(st.index("(") + 1) : (st.index(")"))].strip()
                    f_name = self.correction_name(f_name).strip()
                    return f_name
            else:
                return self.chenge_name(
                    self._path.split("\\")[-1]
                )  # если в файле названия нет - берем имя файла
        # except UnicodeDecodeError as u:
        #     print(u)

    def find_zavod(self):
        return self._path.split("\\")[int(config.get_set_default("number_folder")) - 1]

    def find_folder(self):
        return self._path.split("\\")[int(config.get_set_default("number_folder"))]

    def find_hash(self) -> str:
        BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
        md51 = hashlib.md5()
        with open(self._path, "rb") as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                md51.update(data)
        return md51.hexdigest()

    @staticmethod
    def chenge_name(st):  # удаляем расширение файла
        if st.rfind(".") > 0:
            return st[0 : st.rfind(".")]
        return st

    @staticmethod
    def correction_name(string):  # удаляем символы кроме букв,цифр и точки
        reg = re.compile("[^a-zA-Z0-9. -]")
        a = reg.sub("", string)
        return a.strip().rstrip(".")


# a=ProgFile(r"\\SERVER2016\Docs\УП\УП2\Авеста\FAS4-A25-11-1 Винт\O0425")
# print(a.get_date_of_change())
# print(a.find_hash())
# print(a.find_folder())
