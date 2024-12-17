import telebot
from telebot import types

# Инициализация бота
bot = telebot.TeleBot("7215978807:AAHv7CQEs31qHLOKEQ4PYEaFlZebSdUz7oU")


# # Задание 1: Простое меню с кнопками
# @bot.message_handler(commands=['start'])
# def start_message(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn_hello = types.KeyboardButton("Привет")
#     btn_goodbye = types.KeyboardButton("Пока")
#     markup.add(btn_hello, btn_goodbye)
#     bot.send_message(message.chat.id, "Выберите опцию:", reply_markup=markup)
#
#
# @bot.message_handler(func=lambda message: message.text == "Привет")
# def greet_user(message):
#     user_name = message.from_user.first_name
#     bot.send_message(message.chat.id, f"Привет, {user_name}!")


# Задание 2: Кнопки с URL-ссылками
@bot.message_handler(commands=['links'])
def show_links(message):
    markup = types.InlineKeyboardMarkup()
    btn_news = types.InlineKeyboardButton("Новости", url="https://news.example.com")
    btn_video = types.InlineKeyboardButton("Видео", url="https://video.example.com")
    btn_music = types.InlineKeyboardButton("Музыка", url="https://music.example.com")
    markup.add(btn_news, btn_video, btn_music)
    bot.send_message(message.chat.id, "Выберите ссылку:", reply_markup=markup)


# Задание 3: Динамическое изменение клавиатуры
@bot.message_handler(commands=['dynamic'])
def dynamic_keyboard(message):
    markup = types.InlineKeyboardMarkup()
    btn_show_more = types.InlineKeyboardButton("Показать больше", callback_data="show_more")
    markup.add(btn_show_more)
    bot.send_message(message.chat.id, "Нажмите кнопку ниже:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "show_more")
def show_more_options(call):
    # Создаем новую клавиатуру с двумя опциями
    markup = types.InlineKeyboardMarkup()
    btn_option1 = types.InlineKeyboardButton("Опция 1", callback_data="option1")
    btn_option2 = types.InlineKeyboardButton("Опция 2", callback_data="option2")
    markup.add(btn_option1, btn_option2)

    # Обновляем сообщение с новыми кнопками
    bot.edit_message_text("Выберите опцию:", chat_id=call.message.chat.id, message_id=call.message.message_id,
                          reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "option1")
def option1_selected(call):
    bot.send_message(call.message.chat.id, "Вы выбрали Опцию 1.")


@bot.callback_query_handler(func=lambda call: call.data == "option2")
def option2_selected(call):
    bot.send_message(call.message.chat.id, "Вы выбрали Опцию 2.")

@bot.message_handler(func=lambda message: message.text == "Пока")
def goodbye_user(message):
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f"До свидания, {user_name}!")
# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
