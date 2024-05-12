"""
Файлы в файле 🌶️🌶️
Вам доступен текстовый файл files.txt, содержащий информацию о файлах. Каждая строка файла содержит три значения, разделенные символом пробела — имя файла, его размер (целое число) и единицы измерения:

cant-help-myself.mp3 7 MB
keep-yourself-alive.mp3 6 MB
bones.mp3 5 MB
...
Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы, и выводит полученные группы файлов, указывая для каждой ее общий объем. Группы должны быть расположены в лексикографическом порядке названий расширений, файлы в группах — в лексикографическом порядке их имен.

Примечание 1. Например, если бы файл files.txt имел вид:

input.txt 3000 B
scratch.zip 300 MB
output.txt 1 KB
temp.txt 4 KB
boy.bmp 2000 KB
mario.bmp 1 MB
data.zip 900 MB
то программа должна была бы вывести:

boy.bmp
mario.bmp
----------
Summary: 3 MB

input.txt
output.txt
temp.txt
----------
Summary: 8 KB

data.zip
scratch.zip
----------
Summary: 1 GB
где Summary — общий объем файлов группы.

Примечание 2. Гарантируется, что все имена файлов содержат расширение.

Примечание 3. Общий объем файлов группы записывается в самых крупных (максимально возможных) единицах измерения с округлением до целых. Другими словами, сначала следует определить суммарный объем всех файлов группы, скажем, в байтах, а затем перевести полученное значение в самые крупные (максимально возможные) единицы измерения. Примеры перевода:

1023 B -> 1023 B
1300 B -> 1 KB
1900 B -> 2 KB
Примечание 4. Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB
Примечание 5. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 6. При открытии файла используйте явное указание кодировки UTF-8.
"""


def convert(num, order):
    l = ['B', 'KB', 'MB', 'GB', 'TB']
    unit = {_: l[_] for _ in range(5)}
    if num > 1023:
        num /= 1024
        order += 1
    else:
        return round(num), unit[order]
    return convert(num, order)


dict_size_conversion = {'TB': 'GB', 'GB': 'MB', 'MB': 'KB', 'KB': 'B', 'B': 'B'}
data_input = []
dict_extension = {}
with open('files.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data_input.append(line.strip().replace('.', ' ').split())

for el in data_input:
    if el[1] not in dict_extension:
        dict_extension[el[1]] = [el[0] + '.' + el[1] + ' ' + el[2] + ' ' + el[3]]
    else:
        dict_extension[el[1]].append(el[0] + '.' + el[1] + ' ' + el[2] + ' ' + el[3])

for key in dict_extension.keys():
    dict_extension[key] = sorted(dict_extension[key])

sorted_dict_extension = dict(sorted(dict_extension.items()))

for key in sorted_dict_extension.keys():
    summ_b = 0
    for el in sorted_dict_extension[key]:
        name_memory = el.split()[-1]
        if name_memory == 'B':
            summ_b += int(el.split()[-2])
        elif name_memory == 'KB':
            summ_b += int(el.split()[-2]) * 1024
        elif name_memory == 'MB':
            summ_b += int(el.split()[-2]) * 1024 * 1024
        elif name_memory == 'GB':
            summ_b += int(el.split()[-2]) * 1024 * 1024 * 1024
        print(el.split()[0])
    print('----------')
    num_tuple = convert(summ_b, 1)
    print(f"Summary: {num_tuple[0]} {dict_size_conversion[num_tuple[1]]}")
    print()



