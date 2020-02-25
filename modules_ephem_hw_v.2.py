from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

galaxy = {'Mars': ephem.Mars, 'Venus': ephem.Venus, 'Moon': ephem.Moon, 'Jupiter': ephem.Jupiter, 'Saturn': ephem.Saturn}


def main():
    mybot = Updater("1097577104:AAHoqylJFKEK7HDsanQNHTYW5qtSM-2rjqo", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", start_hello))
    dp.add_handler(CommandHandler("planet", send_planet))

    mybot.start_polling()
    mybot.idle()


def start_hello(bot, update):
    user = update.effective_user
    first_name = user.first_name
    greeting = f'Hello {first_name}'
    print(greeting)
    update.message.reply_text(greeting)
    planet_request = 'Type /planet and its name'
    print(planet_request)
    update.message.reply_text(planet_request)


def send_planet(bot, update):
    user_text = update.message.text
    planet_text = user_text.split(' ')
    planet = planet_text[1]

    if galaxy.get(planet) is not None:
        print(planet)
        update.message.reply_text(planet)
        # import datetime
        # today = datetime.datetime.today()
        # print(today.strftime("%m/%d/%Y"))
        # planet_ephem = getattr(ephem, planet)(today.strftime("%Y/%m/%d"))
        date = ephem.now()
        print(date)
        update.message.reply_text(date)
        planet_ephem = galaxy[planet](date)
        constellation = ephem.constellation(planet_ephem)
        print(constellation)
        update.message.reply_text(constellation)
    else:
        update.message.reply_text(planet)
        no_planet_text = 'There is no such planet in our database'
        print(no_planet_text)
        update.message.reply_text(no_planet_text)


main()