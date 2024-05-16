"""
Функция is_available_date() 🌶️
Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та или иная дата для бронирования номера.

Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:

booked_dates — список строковых дат, недоступных для бронирования. Элементом списка является либо одиночная дата, либо период (две даты через дефис). Например:
['04.11.2021', '05.11.2021-09.11.2021']
date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает забронировать номер. Например:
'01.11.2021' или '01.11.2021-04.11.2021'
Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна для бронирования. В противном случае функция должна возвращать False.

Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.

Примечание 2. В периоде (две даты через дефис) граничные даты включены.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_available_date(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
"""
from datetime import datetime, timedelta


def is_available_date(booked_dates: list, date_for_booking: str):
    flag = True
    for booked_date in booked_dates:
        if '-' not in booked_date:
            if '-' not in date_for_booking:
                if booked_date == date_for_booking:
                    flag = False
                    break
            else:
                two_date_for_booking = date_for_booking.split('-')
                array_date_for_booking = []
                dt_start_date_for_booking = datetime.strptime(two_date_for_booking[0], '%d.%m.%Y')
                dt_start_end_for_booking = datetime.strptime(two_date_for_booking[1], '%d.%m.%Y')
                while True:
                    array_date_for_booking.append(dt_start_date_for_booking)
                    dt_start_date_for_booking = dt_start_date_for_booking + timedelta(days=1)
                    if dt_start_date_for_booking == dt_start_end_for_booking:
                        break
                array_date_for_booking.append(dt_start_date_for_booking)
                dt_booked_date = datetime.strptime(booked_date, '%d.%m.%Y')
                if dt_booked_date in array_date_for_booking:
                    flag = False
                    break
        else:
            if '-' not in date_for_booking:
                two_booked_date = booked_date.split('-')
                array_booked_date = []
                dt_start_booked_date = datetime.strptime(two_booked_date[0], '%d.%m.%Y')
                dt_end_booked_date = datetime.strptime(two_booked_date[1], '%d.%m.%Y')
                while True:
                    array_booked_date.append(dt_start_booked_date)
                    dt_start_booked_date = dt_start_booked_date + timedelta(days=1)
                    if dt_start_booked_date == dt_end_booked_date:
                        break
                array_booked_date.append(dt_start_booked_date)
                dt_date_for_booking = datetime.strptime(date_for_booking, '%d.%m.%Y')
                if dt_date_for_booking in array_booked_date:
                    flag = False
                    break
            else:
                two_booked_date = booked_date.split('-')
                array_booked_date = []
                dt_start_booked_date = datetime.strptime(two_booked_date[0], '%d.%m.%Y')
                dt_end_booked_date = datetime.strptime(two_booked_date[1], '%d.%m.%Y')
                while True:
                    array_booked_date.append(dt_start_booked_date)
                    dt_start_booked_date = dt_start_booked_date + timedelta(days=1)
                    if dt_start_booked_date == dt_end_booked_date:
                        break
                array_booked_date.append(dt_start_booked_date)
                two_date_for_booking = date_for_booking.split('-')
                array_date_for_booking = []
                dt_start_date_for_booking = datetime.strptime(two_date_for_booking[0], '%d.%m.%Y')
                dt_start_end_for_booking = datetime.strptime(two_date_for_booking[1], '%d.%m.%Y')
                while True:
                    array_date_for_booking.append(dt_start_date_for_booking)
                    dt_start_date_for_booking = dt_start_date_for_booking + timedelta(days=1)
                    if dt_start_date_for_booking == dt_start_end_for_booking:
                        break
                array_date_for_booking.append(dt_start_date_for_booking)
                for i in array_booked_date:
                    if i in array_date_for_booking:
                        flag = False
                        break
    return flag
