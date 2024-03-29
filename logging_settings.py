import logging
import telebot
import TFM_settings as _settings



# class TelegramBotHandler(logging.Handler):
#     def __init__(self, token: str, chat_id: str):
#         super().__init__()
#         self.token = token
#         self.chat_id = chat_id

#     def emit(self, record):
#         message = self.format(record)
#         bot = telebot.TeleBot(self.token)
#         try:
#             bot.send_message(self.chat_id,message)
#         except:
#             pass

bot = telebot.TeleBot(_settings.TOKEN)
bot.send_message('-1001577560699','Hello')

# b=logging.basicConfig('ff',)
# a=Teleg('5060398934:AAE0O8b0Op5iNLKIeGNIpCz7Pr-q9tWdTPA','-1001577560699')
# a.emit('hello')