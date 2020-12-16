"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой.
"""


def user_info(name, lastname, birth, city, email, phone):
    """Выводим данные о пользователе одной строкой."""
    print('Пользователь {} {}, дата рождения -  {}, город - {}, email - {}, телефон - {}'.
          format(name, lastname, birth, city, email, phone))


user_data = []
data_count = 6

while len(user_data) != data_count:
    user_data = input('Введите имя, фамилию, год рождения, город проживания, email и телефон пользователя: ').split()

user_name, user_lastname, user_birth, user_city, user_email, user_phone = user_data
user_info(name=user_name, lastname=user_lastname, birth=user_birth, city=user_city, email=user_email, phone=user_phone)
