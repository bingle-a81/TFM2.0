import logging 
# from logging import StreamHandler, Formatter, LogRecord
import smtplib
import telebot
from TFM_settings import config

class TelegramBotHandler(logging.Handler):
    def __init__(self, token: str, chat_id: str):
        super().__init__()
        self.token = token
        self.chat_id = chat_id

    def emit(self, record: logging.LogRecord):
        message = self.format(record)
        bot = telebot.TeleBot(self.token)
        try:
            bot.send_message(self.chat_id,message)
        except:
            pass


class MegaHandler(logging.Handler):
    def __init__(self, filename):
        logging.Handler.__init__(self)
        self.filename = filename

    def emit(self, record: logging.LogRecord):
        message = self.format(record)
        with open(self.filename, 'a') as file:
            file.write(message + '\n')

class MegaEmail(logging.Handler):
    def __init__(self,server,port,email,passwd):
        logging.Handler.__init__(self)
        self.server=server
        self.port=port
        self.email=email
        self.passwd=passwd

    def emit(self, record: logging.LogRecord) :
        message=self.format(record)
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



logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format': {
            'format': '{asctime} - {levelname} - {name} - {message}',
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            # 'filters': ['new_filter'],
        },
        'file': {
            '()': MegaHandler,
            'level': 'INFO',
            'filename': set.LOG_FILE,
            'formatter': 'std_format',
        },
        'file1': {
            '()': MegaHandler,
            'level': 'DEBUG',
            'filename': set.LOG_FILE_DEBUG,
            'formatter': 'std_format',
        },
        'email':{
            '()':MegaEmail,
            'level': 'ERROR',
            'server':set.SERVER,
            'port':set.PORT,
            'email':set.EMAIL,
            'passwd':set.PASSWD,
            'formatter': 'std_format',
        },
        'telegram_handler': {
            '()': TelegramBotHandler,
            'level': 'WARNING',
            'chat_id': set.CHAT_ID,
            'token': set.TOKEN,
            'formatter': 'std_format',
        }

    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'file','email','telegram_handler'],
            # 'propagate': False
        },
        'json_logger': {
            'level': 'DEBUG',
            'handlers': ['console','file'],
        },
        'telega_logger': {
            'level': 'DEBUG',
            'handlers': ['telegram_handler'],
        },
        'pyautogui_logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'file', 'file1'],
        },
        'to_database_logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'file', 'file1'],
        },
        'email_logger':{
            'level': 'DEBUG',
            'handlers': ['email'],
        }

    },
}
