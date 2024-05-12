'''
Корпоративная почта 🌶️
В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая формируется как <имя-фамилия>@beegeek.bzz, например, timyr-guev@beegeek.bzz. При таком подходе существует проблема тёзок. Для решения такой проблемы было решено приписывать справа номер.

Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера), второй — timyr-guev1@beegeek.bzz, третий — timyr-guev2@beegeek.bzz, и так далее.

Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых сотрудников в заранее подготовленном виде (латиницей с символом - между ними). Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

Формат входных данных
На вход программе в первой строке подается целое неотрицательное число
𝑛
n — количество выданных ящиков. В следующих
𝑛
n строках перечислены сами ящики в порядке выдачи, по одному на строке. На следующей строке задано целое неотрицательное число
𝑚
m — количество новых сотрудников, которым нужно раздать корпоративные ящики. Каждая из последующих
𝑚
m строк представляет собой имя и фамилию сотрудника в подготовленном к использованию формате.

Формат выходных данных
Программа должна вывести почтовые ящики (
𝑚
m строк) для новых сотрудников в том порядке, в котором они раздавались.

Примечание. Тестовые данные доступны по ссылкам:

Архив с тестами
GitHub
'''


n = int(input())
existing_mail = [input() for _ in range(n)]
m = int(input())
new_mail = [input() for _ in range(m)]

dict_new_mail_count = {}
dict_new_mail = {}
dict_missing_number = {}

for n_m in new_mail:
    if n_m not in dict_new_mail_count:
        dict_new_mail_count[n_m] = 1
    else:
        dict_new_mail_count[n_m] += 1

for n_m in new_mail:
    if n_m not in dict_new_mail:
        dict_new_mail[n_m] = dict_new_mail.setdefault(n_m, [])
        for ex_m in existing_mail:
            if ex_m.startswith(n_m):
                symbol = ex_m[: ex_m.find('@')][-1]
                if symbol.isdigit():
                    if ex_m[: ex_m.find('@')][-2].isdigit():
                        symbol_1 = ex_m[: ex_m.find('@')][-2] + symbol
                        if n_m not in dict_new_mail:
                            dict_new_mail[n_m] = [int(symbol_1)]
                        else:
                            dict_new_mail[n_m].append(int(symbol_1))
                    else:
                        if n_m not in dict_new_mail:
                            dict_new_mail[n_m] = [int(symbol)]
                        else:
                            dict_new_mail[n_m].append(int(symbol))
                elif symbol.isalpha():
                    if n_m not in dict_new_mail:
                        dict_new_mail[n_m] = [0]
                    else:
                        dict_new_mail[n_m].append(0)

for key in dict_new_mail.keys():
    dict_new_mail[key] = sorted(dict_new_mail[key])

for key in dict_new_mail_count.keys():
    count = 0
    counter = 0
    while True:
        if len(dict_new_mail[key]) == 1:
            if count != dict_new_mail[key][0]:
                if count == 0:
                    print(f'{key}@beegeek.bzz')
                else:
                    print(f'{key}{count}@beegeek.bzz')
            else:
                count += 1
                print(f'{key}{count}@beegeek.bzz')
            count += 1
            counter += 1
            if counter >= dict_new_mail_count[key]:
                break
        elif len(dict_new_mail[key]) > 1:
            if count in dict_new_mail[key]:
                array = [i for i in range(dict_new_mail[key][-1])] + [i for i in range(dict_new_mail[key][-1] + 1,
                                                                                       dict_new_mail[key][-1] + 1 +
                                                                                       dict_new_mail_count[key])]
                for el in array:
                    if el not in dict_new_mail[key]:
                        if el == 0:
                            print(f'{key}@beegeek.bzz')
                        else:
                            print(f'{key}{el}@beegeek.bzz')
                break
        else:
            print(f'{key}@beegeek.bzz')
            break
            