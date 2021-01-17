"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который
будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом
классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для
каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""


class IsNotDigit(Exception):
    """Класс-исключение Проверка число."""

    def __init__(self):
        """Конструктор."""
        self.txt = 'Некорректно указано количество товара. Движение по складу не выполнено!'


class Warehouse:
    """Класс Склад."""

    def __init__(self, name):
        """Конструктор."""
        self.name = name
        self.balance = {}

    def input_to_warehouse(self, customs, count):
        """
        Принять товар на склад.

        :param customs - товар
        :param count - количество товара
        """
        try:
            if isinstance(count, str):
                raise IsNotDigit()
        except IsNotDigit as err:
            print(err.txt)
        else:
            balance = self.balance
            if customs not in balance.keys():
                balance[customs] = 0
            balance[customs] += count

    def output_from_warehouse(self, customs, count):
        """
        Списать товар со склада.

        :param customs - товар
        :param count - количество товара
        """
        try:
            if isinstance(count, str):
                raise IsNotDigit()
        except IsNotDigit as err:
            print(err.txt)
        else:
            balance = self.balance
            if customs not in balance.keys() or balance[customs] < count:
                print(f'Товара {customs} недостаточно на складе {self.name}. Списание невозможно!')
            else:
                balance[customs] -= count

    def get_balance(self):
        """
        Получить остатки на складе.
        """
        balance = self.balance

        print(f'Остатки на складе {self.name}: ')
        for position, count in balance.items():
            print(f'Товар {position} - {count} шт.')


class OfficeEquipment:
    """Класс Офисная техника."""

    def __init__(self, producer, model):
        """Конструктор."""
        self.producer = producer
        self.model = model


class Printer(OfficeEquipment):
    """Класс Принтер."""

    def __init__(self, producer, model, type):
        """Конструктор."""
        self.producer = producer
        self.model = model
        self.type = type

    def __str__(self):
        """Вывести информацию об экземпляре класса."""
        return f"Принтер {self.type} {self.producer} {self.model}"


class Scaner(OfficeEquipment):
    """Класс Сканер."""

    def __init__(self, producer, model, proffesional):
        """Конструктор."""
        self.producer = producer
        self.model = model
        self.professional = proffesional

    def __str__(self):
        """Вывести информацию об экземпляре класса."""
        return f"Сканер {'профессиональный ' if self.professional else 'бытовой'} {self.producer} {self.model}"


class Xerox(OfficeEquipment):
    """Класс Ксерокс."""

    def __init__(self, producer, model, speed):
        """Конструктор."""
        self.producer = producer
        self.model = model
        self.speed = speed

    def __str__(self):
        """Вывести информацию об экземпляре класса."""
        return f"Ксерокс {self.producer} {self.model} {self.speed}"


warehouse = Warehouse('main')
printer = Printer('HP', 'LaserJet', 'лазерный')
scaner = Scaner('Canon', 'scan-all', False)
xerox = Xerox('Xerox', 'very-fast', '1 page/min')

warehouse.input_to_warehouse(printer, 10)
warehouse.input_to_warehouse(scaner, 6)
warehouse.input_to_warehouse(xerox, 3)

warehouse.get_balance()

warehouse.output_from_warehouse(printer, 5)

warehouse.output_from_warehouse(scaner, 60)
warehouse.output_from_warehouse(scaner, 6)

warehouse.output_from_warehouse(xerox, '3')
warehouse.output_from_warehouse(xerox, 3)

warehouse.get_balance()
