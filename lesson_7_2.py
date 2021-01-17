"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""


from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    """Абстрактный класс для коллекции одежды"""

    @abstractmethod
    def calculate_costs(self):
        """
        Получить затраты ткани на составляющие коллекции.
        """

        pass


class Clothes(AbstractClothes):
    """Класс для коллекции одежды"""

    def __init__(self, name):
        """Конструктор"""

        self.name = name
        self.clothes = []

    def add_clothes(self, clothes):
        """
        Добавить одежду в коллекцию.

        :param clothes: значение дочернего класса.
        :return:
        """
        self.clothes.append(clothes)

    @property
    def calculate_costs(self):
        """
        Получить затраты ткани на коллекцию.
        """

        total_costs = 0
        for item in self.clothes:
            total_costs += item.calculate_costs
        return total_costs


class Coat(Clothes):
    """Класс Пальто."""

    def __init__(self, name, size):
        """Конструктор"""
        self.name = name
        self.size = int(size)

    @property
    def calculate_costs(self):
        """
        Получить затраты ткани на пальто.
        """
        return self.size / 6.5 + .5


class Suit(Clothes):
    """Класс Костюм."""

    def __init__(self, name, height):
        """Конструктор"""
        self.name = name
        self.height = int(height)

    @property
    def calculate_costs(self):
        """
        Получить затраты ткани на костюм.
        """
        return 2 * self.height + .3


collection = Clothes('Лошадиная коллеция')
collection.add_clothes(Coat('Лошадиное пальто', 56))
collection.add_clothes(Coat('Лошадиный костюм', 184))

print(f'{collection.name}. Затраты ткани, всего: {collection.calculate_costs:.2f} м')
for item in collection.clothes:
    print(f'- {item.name}, затраты ткани {item.calculate_costs:.2f} м')
