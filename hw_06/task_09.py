# 9) Создать список поездов. Структура словаря: номер поезда,
# пункт и время прибытия, пункт и время отбытия. Вывести все сведения о поездах, время пребывания в пути
# которых превышает 7 часов 20 минут.


import datetime
trains = [
    {
        'number of train': 1,
        'departure_time': datetime.datetime(2019, 4, 1, 6, 10),
        'departure_city': 'Minsk',
        'arrival_time': datetime.datetime(2019, 4, 1, 9, 30),
        'arrival_city': 'Vilnius',
    },
    {
        'number of train': 2,
        'departure_time': datetime.datetime(2019, 4, 1, 11, 40),
        'departure_city': 'Minsk',
        'arrival_time': datetime.datetime(2019, 4, 1, 21, 30),
        'arrival_city': 'Riga',
    },
    {
        'number of train': 3,
        'departure_time': datetime.datetime(2019, 4, 1, 1, 10),
        'departure_city': 'Grodno',
        'arrival_time': datetime.datetime(2019, 4, 1, 12, 30),
        'arrival_city': 'Talinn',
    },
]

for train in trains:
    delta = train['arrival_time'] - train['departure_time']
    if delta >= datetime.timedelta(hours=7, minutes=20):
        print(train)