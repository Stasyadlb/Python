import requests
import csv


# Функция для проверки вещественных чисел
def isfloat(a):
    try:  # если применение перевода в вещественное число
        float(a)
    except ValueError:  # выдает ошибку
        return False  # вернуть False
    return True  # иначе вернуть True


# Функция для отправки запроса и безотказного получения ответа с сервера.
# Нужна на случай, если соединение прервется или не будет получен ответ,
# чтобы код безотказно продолжил отрабатывать базу
def open_url_rosreest(url, head):
    while True:  # пока не будет получен ответ
        try:  # отправлять запрос
            a = requests.get(url.rstrip('\n'), headers=head, verify=False)
        except Exception:  # если ответ не получен
            print('Erorr')  # вывести ошибка
            continue  # попробовать с начала
        else:  # если ответ получен
            return a  # вернуть полученный ответ


# обозначения пользователя для выполнения запросов
headers = {'Accept': '*/*',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36(KHTML, like Gecko) '
                         'Chrome/113.0.0.0 Safari/537.36'
           }

# создание заголовков для таблицы
cad_number = 'Кадастровый номер'
cad_cost = 'Кадастровая стоимость (руб)'
cad_square = 'Площадь (м2)'
cad_cost_m = 'Кадастровая стоимость 1 м2'

# создание файла, в который будет сохраняться нужная информация
with open('cadastrs_info.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(
        (cad_number, cad_cost, cad_square, cad_cost_m)
    )

iteration_counter = 0  # счетчик итераций

# открываем файл со ссылками на страницы с информацией
for cadastr_link in open('cadastrs_url.txt'):
    # открываем страницу росреестра
    rosreestr_page = open_url_rosreest(cadastr_link, headers)

    # если информация об участке отсутствует, переходим к следующему
    if rosreestr_page.text == '{"feature": null}':
        cad_number = '23:49:0' + cadastr_link[46:]

        # предварительно записав в файл кадастровый номер
        with open('cadastrs_info.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow((cad_number, ''))

        iteration_counter += 1
        continue

    # разбиваем полученные данные по блокам,
    # примерно соответствующим парам ключ-значение
    rosreestr_dictionary = rosreestr_page.text.split(', ')

    # в полученных блоках ищем
    for elements_list in rosreestr_dictionary:
        # кадастровый номер
        if elements_list.startswith('"cn": '):
            cad_number = elements_list[6:].strip('"{} ')

        # стоимость участка
        elif elements_list.startswith('"cad_cost": '):
            # если информация есть, записываем ее
            if isfloat(elements_list[12:]):
                cad_cost = float(elements_list[12:])
            # если нет, оставляем строку пустой
            else:
                cad_cost = ''

        # площадь участка, аналогично со стоимостью
        elif elements_list.startswith('"area_value": '):
            # проверяем наличие информации, и если она есть - записываем
            if isfloat(elements_list[14:]):
                cad_square = float(elements_list[14:])
            # если нет - оставляем пустое значение
            else:
                cad_square = ''

    # проверяем наличие информации о стоимости и площади участка
    # если есть, вычисляем стоимость 1 м2
    if (cad_square and cad_cost) != '':
        cad_cost_m = cad_cost / cad_square
    # если нет - оставляем пустое значение
    else:
        cad_cost_m = ''

    # сохранение собранной информации в файл
    with open('cadastrs_info.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            (cad_number, cad_cost, cad_square, cad_cost_m)
        )

    iteration_counter += 1
    print(iteration_counter)
