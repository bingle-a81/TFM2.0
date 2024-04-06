import ftplib

# Параметры подключения к FTP-серверу
server = '192.168.88.40'
username = 'Administrator'
password = 'CNC'

# Подключение к FTP-серверу
try:
    ftp = ftplib.FTP(server)
except Exception as e:
    print('Ошибка подключения к FTP-серверу:', e)
    exit()

# Логинимся на FTP-сервер
try:
    ftp.login(username, password)
except Exception as e:
    print('Ошибка авторизации на FTP-сервере:', e)
    ftp.quit()
    exit()

# Переходим в нужную директорию
try:
    ftp.cwd('/path/to/directory')
except Exception as e:
    print('Ошибка перехода в директорию:', e)
    ftp.quit()
    exit()

# Загрузка файла с локального компьютера на FTP-сервер
local_file = 'local_file.txt'
remote_file = 'remote_file.txt'
with open(local_file, 'rb') as file:
    ftp.storbinary('STOR ' + remote_file, file)

# Выход с FTP-сервера
ftp.quit()

# download_img()


