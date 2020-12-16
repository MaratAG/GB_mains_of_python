"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый
элемент с тем же значением должен разместиться после них.
"""

my_list = [7, 5, 3, 3, 2]

while True:
    users_number = input('Введите натуральное число: ')

    if not(len(users_number)):
        break

    users_number = int(users_number)
    if users_number > 0:
        for index, item in enumerate(my_list):
            if users_number > item:
                my_list.insert(index, users_number)
                break
        else:
            my_list.append(users_number)

        print('Пользователь ввел число {}. Результат {}'.format(users_number, my_list))
    else:
        print('{} - не натуральное число'.format(users_number))
