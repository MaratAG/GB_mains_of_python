"""
6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с
параметрами (характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
"""

goods = []
analytics = {}
count = 0

while True:
    good_info = input('Введите данные по товару (название, цена, количество, ед.измерения): ').split()
    if not (len(good_info)):
        break
    elif len(good_info) == 4:
        count += 1
        goods.append(
            (count,
             {
                 'название': good_info[0],
                 'цена': int(good_info[1]),
                 'количество': int(good_info[2]),
                 'ед': good_info[3]
             }
             )
        )

if len(goods):
    for good in goods:
        chars = good[1]
        for key, item in chars.items():
            if key in analytics.keys():
                analytics[key].add(item)
            else:
                analytics[key] = set([item])

    print('\nАналитика по товарам: ')
    for key, item in analytics.items():
        print('{}: {}'.format(key, list(item)))
