import telebot
from telebot.types import Chat
import time
import requests
from translate import Translator
import datetime as dt
# токен телеграм-бота
token = 'токен'
# токен OpenWeatherApi
weather_token = '4b2f11bf582a82a29f0772230f12c83a'
bot = telebot.TeleBot(token)

# функция получения данных с OpenWeatherMap
def get_weather_data(api_key=weather_token):
    
    # какой город
    place = "Saint Petersburg"
    # ссылка на API
    url = f'http://api.openweathermap.org/data/2.5/forecast/daily?lat=12&lon=12&cnt=5&appid=4b2f11bf582a82a29f0772230f12c83a?'
    res = requests.get(url)
    data = res.json()
    
    # перевод с английского на русский
    translator = Translator(from_lang="en", to_lang="ru")
    place_ru = translator.translate(place)
    weather = translator.translate(data['weather'][0]['description'])
    temp = round(data['main']['temp'] - 273.15)
    wind_speed = data['wind']['speed']
    fells = round(data['main']['feels_like'] - 273.15)
    pres = data['main']['pressure']
    hum = data['main']['humidity']
    
    return(place_ru, weather, temp, wind_speed, fells, pres, hum)
# декоратор для обработки команды /start
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, text=f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>! Я буду отправлять тебе погоду.', parse_mode='html')
    # цикл для ежедневной отправки
    while True:
        # time_start = dt.datetime.now()
        # h = time_start.hour
        # m = time_start.minute
        if True:
            plc, wtr, temp, win_speed, fells, pres, hum = get_weather_data(api_key=weather_token)
            bot.send_message(message.chat.id, text=f'Погода в городе <b>{plc}</b>: <b>{wtr}</b>\nтемпература: <b>{temp} °C</b>, ощущается как <b>{fells} °C</b>\nскорость ветра: <b>{win_speed} м/с</b>\nДавление: <b>{pres}  мм рт.ст.</b>\nВлажность <b>{hum} %</b>', parse_mode='html')
        time.sleep(50)
bot.polling()   
