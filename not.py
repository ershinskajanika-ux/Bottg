import telebot
import os
import time

# Токен берется из переменных Railway
TOKEN = os.environ.get('TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = ("Здравствуйте, меня зовут Александр Гунько.\n"
                    "Я массажист-реабилитолог, преподаватель хатха-йоги и ведущий каналов «Анатомия и Биомеханика».\n"
                    "Нажмите кнопку «Оплата», чтобы получить реквизиты.")
    
    bot.send_message(message.chat.id, welcome_text)
    
    # Создаем кнопки
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton("Рубли", callback_data="rub"))
    keyboard.row(telebot.types.InlineKeyboardButton("PayPal", callback_data="paypal"))
    keyboard.row(telebot.types.InlineKeyboardButton("Евро", callback_data="eur"), 
                 telebot.types.InlineKeyboardButton("Доллар", callback_data="usd"))
    keyboard.row(telebot.types.InlineKeyboardButton("Гривна", callback_data="uah"), 
                 telebot.types.InlineKeyboardButton("USDT в Binance", callback_data="usdt"))
    keyboard.row(telebot.types.InlineKeyboardButton("⬅️ Назад", callback_data="back"))
    
    bot.send_message(message.chat.id, "Выберите удобный способ оплаты:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    chat = call.message.chat.id
    
    # ЗДЕСЬ ВСТАВЬТЕ СВОИ РЕКВИЗИТЫ (измените текст на свои данные)
    if call.data == "rub":
        bot.send_message(chat, "Рубли: карта Сбербанк 1234 5678 9012 3456")
    elif call.data == "paypal":
        bot.send_message(chat, "PayPal: email@example.com")
    elif call.data == "eur":
        bot.send_message(chat, "Евро: IBAN DE12 3456 7890 1234 5678 90")
    elif call.data == "usd":
        bot.send_message(chat, "Доллары: SWIFT CHASUS33, аккаунт 123456789")
    elif call.data == "uah":
        bot.send_message(chat, "Гривна: карта ПриватБанк 1234 5678 9012 3456")
    elif call.data == "usdt":
        bot.send_message(chat, "USDT (TRC20): TXYZ1234567890abcdefghijklmnopqrs")
    elif call.data == "back":
        start(call.message)

if __name__ == "__main__":
    print("Бот запущен!")
    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(5)
