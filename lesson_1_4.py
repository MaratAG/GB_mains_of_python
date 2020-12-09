"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте
цикл while и арифметические операции.
"""

users_number = int(input('Введите целое положительное число: '))

step = 10
max_number = 0
current_number = users_number

while not current_number == 0:
    number = int(current_number % step)
    max_number = number if number > max_number else max_number
    current_number = (current_number - number) / step

print('Самая большая цифра в числе {1} это {0}'.format(max_number, users_number))
