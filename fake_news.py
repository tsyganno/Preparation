"""
FAKE NEWS 🌶️
Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00. Напишите программу, которая принимает на вход текущие дату и время и определяет, сколько времени осталось до выхода курса.

Формат входных данных
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных
Программа должна вывести текст с указанием количества дней и часов, оставшихся до выхода курса, в следующем формате:

До выхода курса осталось: <кол-во дней> дней и <кол-во часов> часов
Если в данном случае количество часов равно нулю, то вывести нужно только дни.

Если количество дней равно нулю, то вывести нужно только часы и минуты в следующем формате:

До выхода курса осталось: <кол-во часов> часов и <кол-во минут> минут
Если в данном случае количество минут равно нулю, то вывести нужно только часы. Аналогично, если количество часов равно нулю, то вывести нужно только минуты.

Если введенные дата и время больше либо равны 08.11.2022 12:00, программа должна вывести текст:

Курс уже вышел!
Примечание 1. Программа должна подбирать правильную форму для существительных «день» и «минута». Для этого можете смело взять свою функцию choose_plural() из этой задачи.

Примечание 2. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
"""

from datetime import datetime


def choose_plural(amount: int, declensions: tuple):
    if str(amount).endswith('0'):
        return f'{amount} {declensions[-1]}'
    elif str(amount).endswith('11') or str(amount).endswith('12') or str(amount).endswith('13') or str(amount).endswith('14'):
        return f'{amount} {declensions[-1]}'
    elif str(amount).endswith('1'):
        return f'{amount} {declensions[-3]}'
    elif str(amount).endswith('2') or str(amount).endswith('3') or str(amount).endswith('4'):
        return f'{amount} {declensions[-2]}'
    else:
        return f'{amount} {declensions[-1]}'


start_of_the_course_time = datetime(day=8, month=11, year=2022, hour=12)
present_time = datetime.strptime(input(), '%d.%m.%Y %H:%M')
time_left = str(start_of_the_course_time - present_time).split()
hour_minute_second = time_left[-1].split(':')
if len(time_left) > 1:
    if '-' in time_left[0]:
        print('Курс уже вышел!')
    elif time_left[0] == '0':
        if hour_minute_second[0] != '0' and hour_minute_second[1] != '00':
            print(f"До выхода курса осталось: {choose_plural(int(hour_minute_second[0]), ('час', 'часа', 'часов'))} и {choose_plural(int(hour_minute_second[1]), ('минута', 'минуты', 'минут'))}")
        elif hour_minute_second[0] != '0' and hour_minute_second[1] == '00':
            print(f"До выхода курса осталось: {choose_plural(int(hour_minute_second[0]), ('час', 'часа', 'часов'))}")
        elif hour_minute_second[0] == '0' and hour_minute_second[1] != '00':
            print(f"До выхода курса осталось: {choose_plural(int(hour_minute_second[1]), ('минута', 'минуты', 'минут'))}")
        else:
            print('Курс уже вышел!')
    else:
        if hour_minute_second[0] != '0':
            print(f"До выхода курса осталось: {choose_plural(int(time_left[0]), ('день', 'дня', 'дней'))} и {choose_plural(int(hour_minute_second[0]), ('час', 'часа', 'часов'))}")
        elif hour_minute_second[0] == '00' and hour_minute_second[1] != '00':
            print(f"До выхода курса осталось: {choose_plural(int(time_left[0]), ('день', 'дня', 'дней'))} и {choose_plural(int(hour_minute_second[1]), ('минута', 'минуты', 'минут'))}")
        else:
            print(f"До выхода курса осталось: {choose_plural(int(time_left[0]), ('день', 'дня', 'дней'))}")
else:
    if hour_minute_second[0] != '0' and hour_minute_second[1] != '00':
        print(f"До выхода курса осталось: {choose_plural(int(hour_minute_second[0]), ('час', 'часа', 'часов'))} и {choose_plural(int(hour_minute_second[1]), ('минута', 'минуты', 'минут'))}")
    elif hour_minute_second[0] != '0' and hour_minute_second[1] == '00':
        print(f"До выхода курса осталось: {choose_plural(int(hour_minute_second[0]), ('час', 'часа', 'часов'))}")
    elif hour_minute_second[0] == '0' and hour_minute_second[1] != '00':
        print(f"До выхода курса осталось: {choose_plural(int(hour_minute_second[1]), ('минута', 'минуты', 'минут'))}")
    else:
        print('Курс уже вышел!')
