import telebot
# Тег бота
bot = telebot.TeleBot('тег вiд botfather')
# /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привіт, напиши шось і я відповім тобі) )')
# Отримання повідомлення від користувача
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Ти написав: ' + message.text)
# Запускаємо бота
bot.polling(none_stop=True, interval=0)