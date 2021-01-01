"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    """Класс Канцелярская принадлежность"""
    title = 'stationery'

    def draw(self):
        """
        Выводит сообщение о запуске отрисовки.

        :return: сообщение
        """

        print(f'Запуск отрисовки.')


class Pen(Stationery):
    """Класс Ручка"""

    def draw(self):
        """
        Выводит сообщение о запуске отрисовки.

        :return: сообщение
        """

        print(f'Запуск отрисовки синей ручкой.')


class Pencil(Stationery):
    """Класс Карандаш"""

    def draw(self):
        """
        Выводит сообщение о запуске отрисовки.

        :return: сообщение
        """

        print(f'Запуск отрисовки чертежным карандашом.')


class Handle(Stationery):
    """Класс Маркер"""

    def draw(self):
        """
        Выводит сообщение о запуске отрисовки.

        :return: сообщение
        """

        print(f'Запуск отрисовки черным маркером.')


pen = Pen()
pen.title = 'ручка'

pencil = Pencil()
pencil.title = 'карандаш'

handle = Handle()
handle.title = 'маркер'

pen.draw()
pencil.draw()
handle.draw()
