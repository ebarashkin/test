import config
import telebot

telegram = api.TelegramBot('601071819:AAGf0OobZXOkfF91VZe6DR_5i60LYXlccSg')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
