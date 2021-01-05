"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""


class Matrix:
    """Класс Матрица"""

    def __init__(self, matrix):
        """Конструктор."""

        self.matrix = self.__convert_to_matrix__(matrix)

    def __convert_to_matrix__(self, matrix):
        """
        Подготовить матрицу на основании входных значений.

        :param matrix - входное значение, получаемое при ининициализации экземпляра класса
        :return result - преобразованное в необходимый вид входное значение
        """

        result = []
        if matrix:
            max_len_of_input_list = max([len(item.split()) for item in matrix])
            for item in matrix:
                input_list = list(map(int, item.split()))
                new_string = [input_list[i] if i < len(input_list) else 0 for i in range(max_len_of_input_list)]
                result.append(new_string)
        else:
            result.append([])

        return result

    def __str__(self):
        """
        Вывод матрицы в привычном для восприятия виде.
        """

        result = ""
        for item in self.matrix:
            result += ' '.join(list(map(str, item))) + '\n'
        return result

    def __add__(self, other):
        """
        Сложение двух матриц.
        """

        input_list = []
        new_matrix = None

        if isinstance(other, Matrix):
            len_of_string = len(self.matrix[0])
            if len(self.matrix) == len(other.matrix) and len_of_string == len(other.matrix[0]):
                for index in range(len(self.matrix)):
                    new_string = [str(self.matrix[index][i] + other.matrix[index][i]) for i in range(len_of_string)]
                    input_list.append(' '.join(new_string))

        if input_list:
            new_matrix = Matrix(input_list)
        else:
            print('Сложение матриц невозможно!')
        return new_matrix


def get_matrix():
    """
    Получить входные данные для создания экземпляра класса Matrix.

    :return: список строк значений для матрицы.
    """

    input_matrix = []
    iterate = 1

    while True:
        string_of_input_matrix = input(f'Введите строку {iterate} матрицы: ')
        if not len(string_of_input_matrix):
            break
        input_matrix.append(string_of_input_matrix)
        iterate += 1

    return input_matrix


print('Введите данные для матрицы 1:')
output_matrix_1 = Matrix(get_matrix())

print('Введите данные для матрицы 2:')
output_matrix_2 = Matrix(get_matrix())
output_matrix_3 = output_matrix_1 + output_matrix_2

print('Матрица 1:')
print(output_matrix_1)

print('Матрица 2:')
print(output_matrix_2)

print('Матрица 3:')
print(output_matrix_3)
