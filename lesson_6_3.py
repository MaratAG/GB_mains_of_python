"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени
сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    """Класс Работник"""

    def __init__(self, name='', surname='', position='', wage=0, bonus=0):
        """Конструктор"""
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus,
        }


class Position(Worker):
    """Класс Должность"""

    def get_full_name(self):
        """Получить полное имя сотрудника.

        :return полное имя сотрудника.
        """

        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income(self):
        """Получить доход с учетом премии.

        :return сумма полного дохода сотрудника (с учетом премии).
        """

        total_income = self._income['wage'] + self._income['bonus']
        return total_income


ivanov = Position('Иван', 'Иванов', 'бухгалтер', 1000, 200)

print(f'Имя: {ivanov.name}, Фамилия: {ivanov.surname} Должность: {ivanov.position}, Доход: {ivanov._income}')

print(f'Полное имя: {ivanov.get_full_name()}')
print(f'Доход: {ivanov.get_total_income():.2f} руб')
