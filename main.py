
import telebot
import datetime
import time
import threading
import random


bot = telebot.TeleBot('BotID')

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.reply_to(message, text="Привет! Я буду напоминать тебе отправить отчет" )
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()


@bot.message_handler(commands=['help'])
def fact_message(message):
    bot.reply_to(message, text=f"Список команд, которые я умею выполнять: \n"
                               f" start - запустить меня \n"
                               f" help - список команд \n"
                               f" rasp - расписание отчетов" )

@bot.message_handler(commands=['rasp'])
def fact_message(message):
    bot.reply_to(message, text=f"Расписание очетов: \n"
                               f" 03:00 \n"
                               f" 07:00 \n"
                               f" 11:00 \n"
                               f" 15:00 \n"
                               f" 19:00 \n"
                               f" 23:00 \n"
                               f" 20:44 для тестов\n")


def send_reminders(chat_id):
    first_rem = "03:00"
    second_rem = "07:00"
    third_rem = "11:00"
    fourth_rem = "15:00"
    fifth_rem = "19:00"
    sixth_rem = "23:00"
    test_rem = "20:44"

    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem or now == second_rem or now == third_rem or now == fourth_rem or now == fifth_rem or now == sixth_rem or now == test_rem:
            bot.send_message(chat_id, "Напоминание: пора отправить отчет!")
            time.sleep(61)
        time.sleep(1)









bot.polling(none_stop=True)


