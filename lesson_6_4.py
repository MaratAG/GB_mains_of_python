"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    """Класс Машина."""

    def __init__(self, speed=0, color='white', name='', is_police=False):
        """Конструктор"""
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        """
        Выводит сообщение о том, что машина начала движение.

        :return: сообщение.
        """

        print(f'Машина {self.name} поехала.')

    def stop(self):
        """
        Выводит сообщение о том, что машина остановилась.

        :return: сообщение.
        """

        print(f'Машина {self.name} остановилась.')

    def turn(self, direction):
        """
        Выводит сообщение о том, что машина повернула.

        :return: сообщение.
        """

        print(f'Машина {self.name} повернула {direction}.')

    def show_speed(self):
        """
        Выводит сообщение о текущей скорсти маширы.

        :return: сообщение.
        """

        print(f'Машина {self.name} - текущая скорость {self.speed} км/ч.')


class TownCar(Car):
    """Класс Городской автомобиль"""

    def show_speed(self):
        """
        Выводит сообщение о текущей скорсти маширы.

        :return: сообщение.
        """

        limit_speed = 60
        print(f'Машина {self.name} - текущая скорость {self.speed} км/ч.')
        if self.speed > limit_speed:
            print(f'Превышение скорости на {self.speed - limit_speed} км/ч!')


class SportCar(Car):
    """Класс Спортивный автомобиль"""


class WorkCar(Car):
    """Класс Спецтехника"""

    def show_speed(self):
        """
        Выводит сообщение о текущей скорсти маширы.

        :return: сообщение.
        """

        limit_speed = 40
        print(f'Машина {self.name} - текущая скорость {self.speed} км/ч.')
        if self.speed > limit_speed:
            print(f'Превышение скорости на {self.speed - limit_speed} км/ч!')


class PoliceCar(Car):
    """Класс Полицейский автомобиль"""


cars = [
    TownCar(100, 'красный', 'Nissan'),
    SportCar(50, 'черный', 'BMW'),
    WorkCar(60, 'желтый', 'BobCat'),
    PoliceCar(30, 'синий', 'Dodge', True),
]

for car in cars:
    print(f'Машина: {car.name}, цвет: {car.color}, это полицейская машина: {"Да" if car.is_police == True else "Нет"}')
    car.go()
    car.turn('налево')
    car.turn('направо')
    car.show_speed()
    car.stop()
    print('')
