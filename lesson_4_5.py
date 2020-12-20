"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
"""

from functools import reduce


def product_list(prev_elm, elm):
    """Возвращает произведение двух значения.

    Parameters
    __________
    prev_elm, elm: int
        Значения, которые необходимо перемножить.
    """
    return prev_elm * elm


start_value = 100
finish_value = 1000
output_list = [item for item in range(start_value, finish_value + 1) if item % 2 == 0]
print(reduce(product_list, output_list))
