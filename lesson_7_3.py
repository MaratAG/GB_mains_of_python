"""
3. Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству клеток (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()),
вычитание (__sub__()),
умножение (__mul__()),
деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""


class Cell:
    """Класс Органическая клетка"""

    def __init__(self, name='', count=1):
        """Конструктор"""
        self.name = name
        self.count = int(count)

    def __str__(self):
        """
        Вывод названия клетки в читабельном виде.
        """
        return f'Клетка {self.name} (ячеек {self.count}).'

    def __add__(self, other):
        """
        Сложение двух клеток.
        """
        if not isinstance(other, Cell):
            return ValueError
        else:
            return Cell(f'{self.name} + {other.name}', self.count + other.count)

    def __sub__(self, other):
        """
        Вычитание двух клеток.
        """
        if not isinstance(other, Cell):
            return ValueError
        else:
            sub_cells = self.count - other.count
            return Cell(f'{self.name} - {other.name}', sub_cells) if sub_cells > 0 else ValueError

    def __mul__(self, other):
        """
        Умножение двух клеток.
        """
        if not isinstance(other, Cell):
            return ValueError
        else:
            return Cell(f'{self.name} * {other.name}', self.count * other.count)

    def __truediv__(self, other):
        """
        Целочисленное деление двух клеток.
        """
        if not isinstance(other, Cell):
            return ValueError
        else:
            div_cells = self.count // other.count
            return Cell(f'{self.name} / {other.name}', div_cells) if div_cells != 0 else ValueError

    def make_order(self, count_in_row):
        """
        Вывод ячеек клетки по рядам.

        :param count_in_row: количество ячеек в ряду.
        :return: строка с разложенными по рядам ячейками.
        """
        slot_in_row = self.count // count_in_row
        slot_in_last_row = self.count % count_in_row
        result = ''
        symbol = '*'
        for iteration in range(slot_in_row):
            result += count_in_row * symbol + '\n'
        result += slot_in_last_row * symbol
        return result


def input_cells():
    """
    Подготовить набор клеток.

    :return: список из экземпляров клсса Cell.
    """

    cells = []
    iteration = 1

    while True:
        count_for_cell = input(f'Введите количество ячеек для клетки №{iteration}: ')
        if not count_for_cell:
            break
        cells.append(Cell(str(iteration), int(count_for_cell)))
        iteration += 1

    return cells


def print_cells(cells):
    """
    Вывод на зкран списка клеток.
    :param cells: список экземпляров класса Cell
    :return:
    """

    print('Набор клеток:')
    for item in cells:
        print(item)


cells = input_cells()
print_cells(cells)

if len(cells) >= 2:
    cells.append(cells[0] + cells[1])
    cells.append(cells[0] - cells[1])
    cells.append(cells[0] * cells[1])
    cells.append(cells[0] / cells[1])

    print_cells(cells)

count_in_row = 12
cell_in_row = cells[0]

print(f'Ячейки клетки {cell_in_row.name}, размещенные в ряд по {count_in_row}: ')
print(cell_in_row.make_order(count_in_row))
