"""
Шахматы были лучше 🌶️
Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов, каждый из которых содержит информацию о каком-либо футболисте:

{
   "first_name": "Gary",
   "last_name": "Cahill",
   "team": "Chelsea",
   "position": "Defender"
}
У футболиста имеются следующие атрибуты:

first_name — имя
last_name — фамилия
team — название футбольного клуба
position — игровая позиция
Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов, выступающих за футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке имен, а при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.

Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует, что он является корректным текстовым файлом в формате JSON. Для того чтобы определить, является ли файл корректным текстовым файлом в формате JSON, воспользуйтесь конструкцией try-except и функцией is_correct_json() из предыдущего урока.

Примечание 2. Начальная часть ответа выглядит так:

Alex Iwobi
Alexis Sanchez
...
Примечание 3. Указанный архив доступен по ссылке. Ответ на задачу доступен по ссылке.
"""


from zipfile import ZipFile
import json

array = []
with ZipFile('data.zip') as zip_file:
    info = zip_file.namelist()
    for el in info:
        last_file = zip_file.getinfo(el)
        if not last_file.is_dir():
            zip_file.extract(el)
            with open(el, encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    if data['team'] == 'Arsenal':
                        array.append((data['first_name'], data['last_name']))
                except:
                    pass
for el in sorted(array, key=lambda x: (x[0], x[1])):
    print(f"{el[0]} {el[1]}")
