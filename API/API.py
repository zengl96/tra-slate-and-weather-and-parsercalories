import requests
from pprint import pprint
import datetime
token = 'e9f9014a96de0057bf3dbb84759baa98'
def get(city,token):
    to = {
        "Clear": "ясно",
        "Clouds": "облачно",
        "Rain": "идет дождь ",
        "Drizzle": "дождь ",
        "Thunderstorm": "гроза",
        "Snow": "снег",
        "Mist": "туман"
    }
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric"
        )
        data = r.json()
        temp = (data['main']['temp'])
        humidity = (data['main']['humidity'])
        pressure = (data['main']['pressure'])
        wind = (data['wind']['speed'])
        n = data["weather"][0]["main"]
        if n in to :
            wd = to[n]
        else:
            wd = 'слишком сложная погода для меня'
        #sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        #sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        #l = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        print(f"______{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}____\n"
              f"Погода в городе: {city}\nТемпература: {temp}C°\n{wd}\n"
              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
              #f"Восход солнца: {sunrise}\nЗакат солнца: {sunset}\nПродолжительность дня: {l}\n"
              f"Хорошего дня!"
              )
    except :
        print(f'похоже города {city} нет в моей базе или город написан не правильно')
def main():
    tex = input('введите слово: ')
    get(tex , token)
if __name__ == '__main__':
    main()

