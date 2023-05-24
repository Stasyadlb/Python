# открываем файл для записи кадастровых номеров
with open('cadastrs_number.txt', 'w') as file:
    # создаем множество, чтобы исключить повторение кадастровых номеров
    a = set()
    # открываем файл с информацией о кадастрах
    for i in open('перечень участков.txt'):
        if i.startswith('23:49:0'):  # если строка начинается с "23:49:"
            if '(' in i:  # если строка содержит (*), удаляем этот элемент
                i = i.split('(')
                i = i[0]
            a.add(i.strip())  # добавляем строку в множество
    # записываем полученное множество с кадастровыми номерами в файл
    file.write('\n'.join(a))
    file.close()

# открываем файл для записи
with open('cadastrs_url.txt', 'w') as file:
    # открываем файл с кадастровыми номерами
    for i in open('cadastrs_number.txt'):
        file.write('https://pkk.rosreestr.ru/api/features/1/'
                   + '23:49:' + i.strip()[7:] + '\n')
        # записываем ссылку на страницу с информацией об участке в файл,
        # убрав незначащий ноль после "23:49:",
        # так как в директории росреестра используется такой формат
    file.close()
