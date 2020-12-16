"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""

number_of_month = int(input("Введите порядковый номер месяца: "))
message = 'не могу определить'

seasons_list = ['зима', 'зима',
                'весна', 'весна', 'весна',
                'лето', 'лето', 'лето', 'осень',
                'осень', 'осень', 'зима']

seasons_dict = {'зима': [12, 1, 2],
                'весна': [4, 5, 6],
                'лето': [6, 7, 8],
                'осень': [9, 10, 11]
                }


if 1 <= number_of_month <= 12:
    message = ' список - {}'.format(seasons_list[number_of_month - 1])
    for key, item in seasons_dict.items():
        if number_of_month in item:
            message += ', словарь - ' + key
            break

print('Время года для месяца с номером {}: {}'.format(number_of_month, message))
