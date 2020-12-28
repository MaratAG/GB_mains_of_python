"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""

from itertools import count as count_value
from itertools import cycle

stop_count = 10

start_value = int(input('Введите число, начиная с которого нужно генерировать целые числа: '))
input_list = input('Введите список значений (через пробел), которые необходимо повторять: ').split()

print('\nИтератор, генерирующий целые числа, начиная с указанного: ')
count = 0
for item in count_value(start_value):
    if count > stop_count:
        break
    print(item, end=' ')
    count += 1

print('\nИтератор, повторяющий элементы некоторого списка, определенного заранее: ')
count = 0
for item in cycle(input_list):
    count += 1
    if count > stop_count * len(input_list):
        break
    print(item, end=' ')
    if count % len(input_list) == 0:
        print('\n', end='')
