"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка.
"""

file_name = 'user_file.txt'

with open(file_name, 'w', encoding='utf-8') as user_file:
    while True:
        user_string = input('Введите строку (окончание ввода - пустая строка): ').strip()
        if not len(user_string):
            break
        else:
            user_file.writelines('{}{}'.format(user_string, '\n'))
