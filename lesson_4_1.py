"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def calculate_salary(elements_of_salary):

    """Рассчитывает размер заработной платы и возвращает расчитанное значение.

    Parameters
    __________
    elements_of_salary: list
        состсавляющие для расчета зарплаты - выработка в часах, ставка в час, премия
    """

    message = 'Недостаточно параметров для расчета заработной платы'
    hours = 0
    price = 0
    bonus = 0

    if len(elements_of_salary) > 2:
        hours = float(elements_of_salary[1])
        price = float(elements_of_salary[2])

        if len(elements_of_salary) > 3:
            bonus = float(elements_of_salary[3])
        salary = hours * price + bonus
        message = 'Заработная плата - {:.2f} USD'.format(salary)
    return message


if __name__ == '__main__':
    print(calculate_salary(argv))
