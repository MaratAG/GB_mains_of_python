"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
 аргументов.
"""


def my_func(*args):
    """Возвращает сумму аргументов (не включая минимального)."""
    args = list(map(int, args))
    args.sort()
    return sum(args[1:])


a, b, c = input('Введите аргументы a, b, c: ').split()
print('Сумма наибольших двух аргументов: {}'.format(my_func(a, b, c)))
