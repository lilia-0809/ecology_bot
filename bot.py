import telebot
import random
import os
print(os.listdir('images'))

bot = telebot.TeleBot('8253309841:AAGfHqHtSwzZJuj4FYtxdnZcrOiZz-AKz1Y')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Используйте команды list;food;carton;paper;iron;wood;brick;plastic;aluminum;glass, чтобы получить подсказку!")

@bot.message_handler(commands=['food'])
def start_command(message):
    bot.send_message(message.chat.id, "пищевые остатки разлогаются до 12 месяцев")

@bot.message_handler(commands=['carton'])
def start_command(message):
    bot.send_message(message.chat.id, "картон разлогается год")


@bot.message_handler(commands=['paper'])
def start_command(message):
    bot.send_message(message.chat.id, "бумага разлогается 2 года")


@bot.message_handler(commands=['iron'])
def start_command(message):
    bot.send_message(message.chat.id, "железо включая банки разлогается 10 лет")

@bot.message_handler(commands=['wood'])
def start_command(message):
    bot.send_message(message.chat.id, "дерево включая доски разлогается 10 лет")

@bot.message_handler(commands=['brick'])
def start_command(message):
    bot.send_message(message.chat.id, "керпичи и бетон разлогаются более 10 лет")

@bot.message_handler(commands=['plastic'])
def start_command(message):
    bot.send_message(message.chat.id, "пластик разлогается 200 лет")

@bot.message_handler(commands=['aluminum'])
def start_command(message):
    bot.send_message(message.chat.id, "алюминий разлогается 500 лет")

@bot.message_handler(commands=['glass'])
def start_command(message):
    bot.send_message(message.chat.id, "стекдо разлогается 1 тысячу лет")

@bot.message_handler(commands=['list'])
def send_list(message):
    with open('images/list.png', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['fact'])
def send_list(message):
    img_name = random.choice(os.listdir('images'))  # Случайным образом выбираем изображение
    with open(f'images/{img_name}', 'rb') as f:
        # Отправляем фото, выбранное случайным образом
        bot.send_photo(message.chat.id, f)


bot.polling()
