import keyboard
import win32api 
import os    
import AppOpener   
import time
import smtplib

print('''SHKV.416001.100.055:
  adress: "\u0422\u0435\u043C\u043F-\u0410\u0432\u0438\u0430\\\u0428\u0418\u041A\u0412\
    .416001.100.055 \u0428\u0435\u0441\u0442\u0435\u0440\u043D\u044F \u0446\u0435\u043D\
    \u0442\u0440\u0430\u043B\u044C\u043D\u0430\u044F"
  prog:
  - - SHKV.416001.100.055.NC
    - 46de95f172595c07ef0203358fde2eae
  - - SHKV.416001.100.055.NC
    - 2f1da56637e351738f7e894e8231a198
  - - $2$SHKV.416001.100.055.NC
    - d6c647df9b57688415549e9e1919cd35
  - - SHKV.416001.100.055.NC
    - 726954839823504aeabf1583253e34fc
  - - SHKV.416001.100.055.NC
    - d7c64ae999306d758a49056203bf7237
''')

# class SendEmail():
#     def __init__(self,server,port,email,passwd):
#         self.server=server
#         self.port=port
#         self.email=email
#         self.passwd=passwd

#     def emit(self, file_name: str) :
#         with open(file_name,'r') as f:
#             message=f.read()
#         charset = f'Content-Type: text/plain; charset=utf-8'
#         mime = 'MIME-Version: 1.0'
#         body = "\r\n".join((f"From: {self.email}", f"To: {self.email}",
#                             f"Subject: File log debug.log ", mime, charset, "", message))
#         # формируем тело письма
#         try:
#             # подключаемся к почтовому сервису
#             smtp = smtplib.SMTP(self.server, self.port)
#             smtp.starttls()
#             smtp.ehlo()
#             # логинимся на почтовом сервере
#             smtp.login(self.email,self.passwd)
#             # пробуем послать письмо
#             smtp.sendmail(self.email, self.email,body.encode('utf-8'))
#         except smtplib.SMTPException as err:
#             print('Что - то пошло не так...')
#             raise err
#         finally:
#             smtp.quit()

# p=SendEmail('smtp.mail.ru','25','bingle_mail@mail.ru','F4JHSWRB76Kvd6bJtUn7')
# p.emit('c:\\Users\\breat\\OneDrive\\Рабочий стол\\pro\\STANKI\\.log\\10.03-12.04.2024-debug.log')


# keyboard.wait('space')
# print (win32api.GetCursorPos())      

# AppOpener.open("filecontrol")  
# time.sleep(5)
# AppOpener.close("filecontrol")                                        