"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
 аргументов.
"""


def my_func(a, b, c):
    """Возвращает сумму аргументов (не включая минимального)."""
    whole_sum = a + b + c
    min_number = a

    min_number = b if whole_sum - (a + c) < min_number else min_number
    min_number = c if whole_sum - (a + b) < min_number else min_number
    sum_without_min = whole_sum - min_number

    return sum_without_min


args = input('Введите аргументы a, b, c: ').split()
a, b, c = list(map(int, args))
print('Сумма наибольших двух аргументов: {}'.format(my_func(a, b, c)))
