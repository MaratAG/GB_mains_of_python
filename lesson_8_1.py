"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    """Класс Дата"""
    date = ''

    def __init__(self, input_date):
        """Конструктор"""
        Date.date = input_date

    @classmethod
    def recognize_date(cls):
        """
        Извлечь число, месяц и год из cls.date и преобразовать к типу Int.

        :return список, состоящий из числа, месяца и года.
        """
        return list(map(int, cls.date.split('-')))

    @staticmethod
    def it_leap_year(validate_year):
        """
        Прроверить, високосный это год или нет.

        :return True - високосный, False - обычный
        """
        result = False
        if (validate_year % 100 == 0 and validate_year % 400 == 0) or (validate_year % 4 == 0):
            result = True
        return result

    @staticmethod
    def validate_date():
        """
        Провести валидацию корректности даты, хранящейся в cls.date.

        :return: True - дата корректна, False - есть ошибки.
        """
        result = True
        months_days = {31: [1, 3, 5, 7, 8, 11, 12],
                       30: [4, 6, 10]}
        day, month, year = Date.recognize_date()
        if not 1980 <= year <= 2099:
            result = False
        elif day == 29 and month == 2 and not Date.it_leap_year(year):
            result = False
        elif not 1 <= month <= 12:
            result = False
        elif (day == 31 and day not in months_days[31]) or (day == 30 and day not in months_days[30]):
            result = False

        return result


init_date = Date('29-02-2021')
print(f'Числа, извлеченные из даты: {Date.recognize_date()}')
print(f'Корректность даты: {Date.validate_date()}')
