import keyboard
import win32api 
import os    
import AppOpener   
import time
import smtplib

class SendEmail():
    def __init__(self,server,port,email,passwd):
        self.server=server
        self.port=port
        self.email=email
        self.passwd=passwd

    def emit(self, file_name: str) :
        with open(file_name,'r') as f:
            message=f.read()
        charset = f'Content-Type: text/plain; charset=utf-8'
        mime = 'MIME-Version: 1.0'
        body = "\r\n".join((f"From: {self.email}", f"To: {self.email}",
                            f"Subject: File log debug.log ", mime, charset, "", message))
        # формируем тело письма
        try:
            # подключаемся к почтовому сервису
            smtp = smtplib.SMTP(self.server, self.port)
            smtp.starttls()
            smtp.ehlo()
            # логинимся на почтовом сервере
            smtp.login(self.email,self.passwd)
            # пробуем послать письмо
            smtp.sendmail(self.email, self.email,body.encode('utf-8'))
        except smtplib.SMTPException as err:
            print('Что - то пошло не так...')
            raise err
        finally:
            smtp.quit()

p=SendEmail('smtp.mail.ru','25','bingle_mail@mail.ru','F4JHSWRB76Kvd6bJtUn7')
p.emit('c:\\Users\\breat\\OneDrive\\Рабочий стол\\pro\\STANKI\\.log\\10.03-12.04.2024-debug.log')


# keyboard.wait('space')
# print (win32api.GetCursorPos())      

# AppOpener.open("filecontrol")  
# time.sleep(5)
# AppOpener.close("filecontrol")                                        