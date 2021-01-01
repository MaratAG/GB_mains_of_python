"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
"""


class Road:
    """Класс Дорога"""

    def __init__(self, length=0, width=0):
        """Конструктор"""
        self._length = length
        self._width = width

    def calculate_costs(self, specific_weight, depth_of_road):
        """Рассчитать затраты асфальта.

        :param specific_weight: масса асфальта для покрытия одного метра дороги (в кг).
        :param depth_of_road: толщина дорожного полотнка в см.

        :return необходимое количество асфальта в тоннах.
         """

        costs_of_asphalt = (self._length * self._width * specific_weight * (depth_of_road / 100)) / 1000
        return costs_of_asphalt


road = Road(5000, 20)

weight_asphalt = 25
depth_asphalt = 5

print(f'Масса асфальта, необходимого для покрытия дороги - {road.calculate_costs(weight_asphalt, depth_asphalt)} т.')
