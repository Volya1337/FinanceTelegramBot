import telebot
import requests
import tkn
import datetime
from currency import gbp, usd, eur
from crypto import btc, eth, doge
from cbrf.models import DailyCurrenciesRates

bot = telebot.TeleBot(tkn.token)
time = datetime.datetime.today().strftime("%d/%m/%Y  %H:%M ")
daily = DailyCurrenciesRates()


# Команда /start - запуск бота
@bot.message_handler(commands=["start"])
def handle_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    keyboard.row("Финансовые новости 📰",)
    keyboard.row("Курс валют ЦБ РФ на сегодня 📈", "Курс криптовалюты на сегодня 📈")
    bot.send_message(message.from_user.id, "Выберите нужную кнопку на клавиатуре, "
                                           "либо введите одну из доступных комманд", reply_markup=keyboard)


# Команда /help - проверка доступных команд
@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.send_message(message.from_user.id, "Доступные комманды:\n\n"
                                               "/start - начало работы с ботом\n"
                                               "/usd, /eur, /gbp - курс валюты на сегодня\n"
                                               "/btc, /eth, /doge - курс крипртовалюты на сегодня\n"
                                               "/usdrub, /eurrub, /gbprub - конвертация валют")


# Команда /list - просмотр всей доступоной валюты и криптовалюты
@bot.message_handler(commands=["list"])
def handle_list(message):
    bot.send_message(message.from_user.id, "Доступные валюты:\n\n"
                                           "USD - доллар США\n"
                                           "EUR - евро\n"
                                           "GBP - Британский фунт\n\n"
                                           "Доступная криптовалюта:\n\n"
                                           "BTC - биткоин\n"
                                           "ETH - эфир\n"
                                           "DOGE - доги")


# Запуск конвертера
@bot.message_handler(commands=["usdrub"])
def usdrub(message):
    send = bot.send_message(message.chat.id, "Введите количество USD, чтобы конвертировать их в RUB")
    bot.register_next_step_handler(send, value)


def value(message):
    count = message.text
    usdconv = daily.get_by_id('R01235').value
    usdconv = float(usdconv)
    while True:
        try:
            bot.send_message(message.chat.id, "Сумма в USD будет составлять {count} RUB".format(
                count=float(count) * usdconv))
        except:
            bot.send_message(message.chat.id, 'Необходимо ввести именно число')
        finally:
            break


@bot.message_handler(commands=["eurrub"])
def eurrub(message):
    send = bot.send_message(message.chat.id, "Введите количество EUR, чтобы конвертировать их в RUB")
    bot.register_next_step_handler(send, value1)


def value1(message):
    count1 = message.text
    eurconv = daily.get_by_id('R01239').value
    eurconv = float(eurconv)
    while True:
        try:
            bot.send_message(message.chat.id, "Сумма в EUR будет составлять {count1} RUB" .format(
                count1=float(count1) * eurconv))
        except:
            bot.send_message(message.chat.id, 'Необходимо ввести именно число')
        finally:
            break


@bot.message_handler(commands=["gbprub"])
def gbprub(message):
    send = bot.send_message(message.chat.id, "Введите количество GBP, чтобы конвертировать их в RUB")
    bot.register_next_step_handler(send, value2)


def value2(message):
    count2 = message.text
    gbpconv = daily.get_by_id('R01035').value
    gbpconv = float(gbpconv)
    while True:
        try:
            bot.send_message(message.chat.id, "Сумма в EUR будет составлять {count2} RUB".format(
                count2=float(count2) * gbpconv))
        except:
            bot.send_message(message.chat.id, 'Необходимо ввести именно число')
        finally:
            break


# Комманды, чтобы проверить курсы валют
@bot.message_handler(commands=["usd"])
def handle_usd(message):
    bot.send_message(message.from_user.id, "На " + str(time) + " цена 1 USD составляет: " + str(usd) + " RUB")


@bot.message_handler(commands=["eur"])
def handle_eur(message):
    bot.send_message(message.from_user.id, "На " + str(time) + " цена 1 EUR составляет: " + str(eur) + " RUB")


@bot.message_handler(commands=["gbp"])
def handle_gbp(message):
    bot.send_message(message.from_user.id, "На " + str(time) + " цена 1 GBP составляет: " + str(gbp) + " RUB")


# Комманды, чтобы проверить курсы криптовалют
@bot.message_handler(commands=["btc"])
def handle_btc(message):
    bot.send_message(message.from_user.id, "На " + str(time) + " цена 1 BTC составляет: " + str(btc()) + " USD")


@bot.message_handler(commands=["eth"])
def handle_eth(message):
    bot.send_message(message.from_user.id, "На " + str(time) + " цена 1 ETH составляет: " + str(eth()) + " USD")


@bot.message_handler(commands=["doge"])
def handle_doge(message):
    bot.send_message(message.from_user.id, "На " + str(time) + " цена 1 DOGE составляет: " + str(doge()) + " USD")


# Основная клавиатура
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Финансовые новости 📰":
        url = "https://news.yandex.ru/finances.html"
        requests.get(url)
        bot.send_message(message.from_user.id, url)
    elif message.text == "Курс валют ЦБ РФ на сегодня 📈":
        keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard1.row("USD 🇺🇸", "GBP 🇬🇧", "EUR 🇪🇺")
        keyboard1.row("🔙 Назад")
        bot.send_message(message.from_user.id, "Выберите валюту", reply_markup=keyboard1)
    elif message.text == "USD 🇺🇸":
        bot.send_message(message.from_user.id, "На " + str(time) + " цена 1 USD составляет: " + str(usd) + " RUB")
    elif message.text == "GBP 🇬🇧":
        bot.send_message(message.from_user.id, "На " + str(time) + " цена 1 GBP составляет: " + str(gbp) + " RUB")
    elif message.text == "EUR 🇪🇺":
        bot.send_message(message.from_user.id, "На " + str(time) + " цена 1 EUR составляет: " + str(eur) + " RUB")
    elif message.text == "🔙 Назад":
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row("Финансовые новости 📰", )
        keyboard.row("Курс валют ЦБ РФ на сегодня 📈", "Курс криптовалюты на сегодня 📈")
        bot.send_message(message.from_user.id, "Выберите дейсвтие", reply_markup=keyboard)
    elif message.text == "Курс криптовалюты на сегодня 📈":
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard2.row("BTC", "ETH", "DOGE")
        keyboard2.row("🔙 Назад")
        bot.send_message(message.from_user.id, "Выберите валюту", reply_markup=keyboard2)
    elif message.text == "BTC":
        bot.send_message(message.from_user.id, "На " + str(time) + " цена 1 BTC составляет: " + str(btc()) + " USD")
    elif message.text == "ETH":
        bot.send_message(message.from_user.id, "На " + str(time) + " цена 1 ETH составляет: " + str(eth()) + " USD")
    elif message.text == "DOGE":
        bot.send_message(message.from_user.id, "На " + str(time) + " цена 1 DOGE составляет: " + str(doge()) + " USD")
    elif message.text == "🔙 Назад":
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row("Финансовые новости 📰", )
        keyboard.row("Курс валют ЦБ РФ на сегодня 📈", "Курс криптовалюты на сегодня 📈")
        bot.send_message(message.from_user.id, "Выберите дейсвтие", reply_markup=keyboard)


# беспрерывная работа скрипта
bot.polling(none_stop=True, interval=0)
