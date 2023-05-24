from prettytable import PrettyTable
# импорт модуля для красивого оформления результата


# Проверка на правильность введенного дробного числа
def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# список спортивных разрядов в формате буквенных сокращений
sports_ranks = ['БСР', 'ТЮР', 'ВЮР', 'ПЮР', 'ТСР', 'ВСР', 'ПСР', 'КМС', 'МС']
# список спортивных разрядов, которые можно получить
sports_d_ranks = ['ТЮР', 'ВЮР', 'ПЮР', 'ТСР', 'ВСР', 'ПСР', 'КМС', 'МС']
# заголовки для столбцов таблицы
table = PrettyTable([' ', 'Фамилия', 'Имя', 'Разряд', 'Получаемый разряд',
                     'Пол', 'Возраст', 'Баллы (Произвольная)',
                     'Баллы (Короткая)', 'Нарушения (Произвольная)',
                     'Нарушения (Короткая)', 'Итоговые баллы (Произвольная)',
                     'Итоговые баллы (Короткая)', 'Итоговый разряд'])

#условия получения каждого разряда для ж и м:
# возраст, баллы произвольная или (произвольная, короткая) программы
for_rank = [{'ТЮР': [6, (7, '-')], 'ВЮР': [6, (11, '-')],
             'ПЮР': [6, (13, '-')], 'ТСР': [8, (16, '-')],
             'ВСР': [9, (19, 13)], 'ПСР': [10, (30, 19)],
             'КМС': [13, (49, 30)], 'МС': [14, (53, 35)]},
            {'ТЮР': [6, (7, '-')], 'ВЮР': [6, (11, '-')],
             'ПЮР': [6, (13, '-')], 'ТСР': [8, (16, '-')],
             'ВСР': [9, (19, 13)], 'ПСР': [10, (30, 19)],
             'КМС': [13, (50, 32)], 'МС': [14, (63, 38)]}]

# использование переменной "а" в качестве переменной для введенных данных
a = input('Введите количество спортсменов: ')
# Проверка на правильность введенных данных:
while True:
    if not (a.isdigit() and int(a) > 0):  # число, больше нуля
        a = input('Вы допустили ошибку при вводе. '
                  'Пожалуйста, введите целое количество спортсменов: ')
    else:
        break
# Сохранение информации о количестве спортсменов
sportsmen_number = int(a)

# Проверка возможности получения разряда для указанного числа спортсменов
for i in range(sportsmen_number):
    s = [i + 1]

    a = input(f'Введите фамилию {i + 1} спортсмена: ')
    # Проверка на правильность введенных данных: введены только буквы
    while True:
        if not a.isalpha():
            a = input(f'Вы допустили ошибку при вводе. Пожалуйста, введите '
                      f'фамилию {i + 1} спортсмена без пробелов и цифр: ')
        else:
            break
    # Сохранение информации о фамилии спортсмена в списке
    s.append(a.upper())

    a = input(f'Введите имя {i + 1} спортсмена: ')
    # Проверка на правильность введенных данных: введены только буквы
    while True:
        if not a.isalpha():
            a = input(f'Вы допустили ошибку при вводе. Пожалуйста, введите '
                      f'имя {i + 1} спортсмена без пробелов и цифр: ')
        else:
            break
    # Сохранение информации об имени спортсмена
    s.append(a.upper())

    a = input(f'Введите текущий разряд {i + 1} спортсмена'
              f' в формате буквенных сокращений: ')
    # Проверка на правильность введенных данных:
    while True:
        # введены только буквы, верно указан разряд
        if not (a.isalpha() and a.upper() in sports_ranks):
            a = input(f'Вы допустили ошибку при вводе. Введите текущий разряд'
                      f' {i + 1} спортсмена в формате буквенных сокращений '
                      f'(БСР, ТЮР, ВЮР, ПЮР, ТСР, ВСР, ПСР, КМС, МС): ')
        else:
            break
    # Сохранение информации о разряде спортсмена
    s.append(a.upper())

    a = input(f'Введите разряд, который хочет получить {i + 1} '
              f'спортсмен, в формате буквенных сокращений: ')
    # Проверка на правильность введенных данных:
    while True:
        # введены только буквы, верно указан разряд
        if not (a.isalpha() and a.upper() in sports_d_ranks):
            a = input(f'Вы допустили ошибку при вводе. Введите разряд, '
                      f'который хочет получить {i + 1} спортсмен, в '
                      f'формате буквенных сокращений (ТЮР, ВЮР, ПЮР, '
                      f'ТСР, ВСР, ПСР, КМС, МС): ')
        else:
            break
    # Сохранение информации о получаемом разряде спортсмена
    s.append(a.upper())

    a = input(f'Введите пол {i + 1} спортсмена (м/ж): ')
    # Проверка на правильность введенных данных:
    while True:
        # введена только одна буква в любом регистре: м/ж
        if not (a.upper() in 'МЖMF' and len(a) == 1):
            a = input(f'Вы допустили ошибку при вводе. '
                      f'Введите пол {i + 1} спортсмена (м/ж): ')
        else:
            break
    # Сохранение информации о поле
    s.append(a.upper())

    a = input(f'Введите возраст {i + 1} спортсмена: ')
    # Проверка на правильность введенных данных:
    while True:
        # число, больше шести
        if not (a.isdigit() and int(a) > 6):
            a = input(f'Вы допустили ошибку при вводе. Пожалуйста, введите '
                      f'возраст {i + 1} спортсмена (целое число, больше 6): ')
        else:
            break
    # Сохранение информации о возрасте
    s.append(int(a))

    a = input(f'Введите полученные {i + 1} спортсменом '
              f'баллы за произвольную программу: ')
    # Проверка на правильность введенных данных:
    while True:
        # вещественное число, больше нуля
        if not (isfloat(a) and float(a) > 0):
            a = input(f'Пожалуйста, введите полученные {i + 1} спортсменом'
                      f' баллы за произвольную программу через точку: ')
        else:
            break
    # Сохранение информации о баллах за произвольную программу
    s.append(float(a))

    if s[4] == 'ВСР' or s[4] == 'ПСР' or s[4] == 'КМС' or s[4] == 'МС':
        a = input(f'Введите полученные {i + 1} спортсменом '
                  f'баллы за короткую программу: ')
        # Проверка на правильность введенных данных:
        while True:
            # вещественное число, больше нуля
            if not (isfloat(a) and float(a) > 0):
                a = input(f'Пожалуйста, введите полученные {i + 1} спортсмено'
                          f'м баллы за короткую программу через точку: ')
            else:
                break
        # Сохранение информации о баллах за произвольную программу
        s.append(float(a))
    else:
        s.append('-')

    a = input(f'Введите вычтенные за нарушения баллы у {i + 1}'
              f' спортсмена (произвольная программа): ')
    # Проверка на правильность введенных данных:
    while True:
        # вещественное число, больше или равно нулю
        if not (isfloat(a) and float(a) >= 0):
            a = input(f'Пожалуйста, введите вычтенные за нарушения баллы у '
                      f'{i + 1} спортсмена (произвольная программа) '
                      f'через точку: ')
        else:
            break
    # Сохранение информации вычтенных о баллах за произвольную программу
    s.append(float(a))

    if s[4] == 'ВСР' or s[4] == 'ПСР' or s[4] == 'КМС' or s[4] == 'МС':
        a = input(f'Введите вычтенные за нарушения баллы у '
                  f'{i + 1} спортсмена (короткая программа): ')
        # Проверка на правильность введенных данных:
        while True:
            # вещественное число, больше или равно нулю
            if not (isfloat(a) and float(a) >= 0):
                a = input(f'Пожалуйста, введите вычтенные за нарушения баллы '
                          f'у {i + 1} спортсмена (короткая программа)'
                          f' через точку: ')
            else:
                break
        # Сохранение информации вычтенных о баллах за короткую программу
        s.append(float(a))
    else:
        s.append('-')

    # Если итоговые баллы за произвольную программу меньше нуля
    if s[7] - s[9] < 0:
        s.append(0.0)  # Итог равен нулю
    # Иначе: разности полученным и вычитаемым за нарушения баллам
    else:
        # Сохранение информации итоговых о баллах за произвольную программу
        s.append(s[7] - s[9])

    # Если итоговые баллы за короткую программу меньше нуля
    if (s[4] == 'ВСР' or s[4] == 'ПСР' or s[4] == 'КМС'
        or s[4] == 'МС') and s[8] - s[10] < 0:
        s.append(0.0)  # Итог равен нулю
    # Иначе: разности полученным и вычитаемым за нарушения баллам
    elif s[4] == 'ВСР' or s[4] == 'ПСР' or s[4] == 'КМС' or s[4] == 'МС':
        s.append(s[8] - s[10])
    # Сохранение информации итоговых о баллах за короткую программу
    else:
        s.append('-')

    sr = sports_ranks.index(s[3])
    d = sports_d_ranks.index(s[4])
    # Условие для получения всех разрядов и отдельно для получения МС и ТЮР
    if ((sr == d or sr - 1 == d or s[3] == 'БСР')
        and not (s[4] == 'МС' or s[4] == 'ТЮР')) \
            or (s[4] == 'МС' and (s[3] == 'КМС' or s[3] == 'МС')) \
            or (s[4] == 'ТЮР' and (s[3] == 'БСР' or s[3] == 'ТЮР')):

        # Проверка получения разрядов для женщин
        if s[5] == 'Ж':
            # Проверка соответствия возраста спортсмена
            if s[6] >= for_rank[0][s[4]][0]:
                # Проверка соответствия баллов для разрядов до ВСР
                if not (s[4] == 'ВСР' or s[4] == 'ПСР' or s[4] == 'КМС'
                        or s[4] == 'МС') and for_rank[0][s[4]][1][0] <= s[11]:
                    # Разряд повышен
                    s.append(s[4])
                    print(f'Спортивный разряд спортсмена повышен до {s[4]}.')

                # Проверка соответствия баллов для разрядов от ВСР
                elif (s[4] == 'ВСР' or s[4] == 'ПСР' or s[4] == 'КМС'
                      or s[4] == 'МС') and for_rank[0][s[4]][1][0] <= s[11] \
                        and for_rank[0][s[4]][1][1] <= s[12]:
                    s.append(s[4])  # Разряд повышен
                    print(f'Спортивный разряд спортсмена повышен до {s[4]}.')

                # Разряд остается неизменным
                else:
                    print('Спортивный разряд не может быть получен: '
                          'спортсмен не набрал нужное количество баллов.')
                    s.append(f'{s[3]} (без изменений)')

            # Разряд остается неизменным
            else:
                print('Спортивный разряд не может быть получен: '
                      'возраст спортсмена не соответствует требованиям.')
                s.append(f'{s[3]} (без изменений)')

        # Проверка получения разрядов для мужчин
        else:
            # Проверка соответствия возраста спортсмена
            if s[6] >= for_rank[1][s[3]][0]:
                # Проверка соответствия баллов для разрядов до ВСР
                if not (s[4] == 'ВСР' or s[4] == 'ПСР' or s[4] == 'КМС'
                        or s[4] == 'МС') and for_rank[1][s[4]][1][0] <= s[11]:
                    # Разряд повышен
                    s.append(s[4])
                    print(f'Спортивный разряд спортсмена повышен до {s[4]}.')

                # Проверка соответствия баллов для разрядов от ВСР
                elif (s[4] == 'ВСР' or s[4] == 'ПСР' or s[4] == 'КМС'
                      or s[4] == 'МС') and for_rank[1][s[4]][1][0] <= s[11] \
                        and for_rank[1][s[4]][1][1] <= s[12]:
                    # Разряд повышен
                    s.append(s[4])
                    print(f'Спортивный разряд спортсмена повышен до {s[4]}.')

                # Разряд остается неизменным
                else:
                    print('Спортивный разряд не может быть получен: '
                          'спортсмен не набрал нужное количество баллов.')
                    s.append(f'{s[3]} (без изменений)')

            # Разряд остается неизменным
            else:
                print('Спортивный разряд не может быть получен: '
                      'возраст спортсмена не соответствует требованиям.')
                s.append(f'{s[3]} (без изменений)')
    # Разряд остается неизменным
    else:
        print('Спортивный разряд не может быть получен: '
              'текущий разряд не соответствует требованиям.')
        s.append(f'{s[3]} (без изменений)')
    # Добавление записанной информации в итоговую таблицу
    table.add_row(s)

a = input(f'Вывести итоговую таблицу участников? ')
# Проверка на правильность введенных данных:
while True:
    # введено "да" или "нет"
    if not (a.upper() == "ДА" or a.upper() == "НЕТ"):
        a = input(f'Пожалуйста, введите "да" или "нет". '
                  f'Вывести итоговую таблицу участников? ')
    else:
        break

if a.upper() == "ДА":
    print(table)

print(f'Конец спортивной комиссии.')
