"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class IsNotComplex(Exception):
    """Класс-исключение Проверка, является ли значение экземпляром класса Complex."""

    def __init__(self):
        """Конструктор."""
        self.txt = 'Оба числа должны быть комплексными. Операция не выполнена!'


class Complex:
    """Класс Комплексное число."""

    def __init__(self, real, imaginary):
        """Конструктор."""
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        """Вывести комплексное число в привычном виде."""
        return f'{self.real} {"+" if self.imaginary >= 0 else "-"} {abs(self.imaginary)}i'

    def __add__(self, other):
        """"Сложение комплексных чисел."""
        try:
            if not isinstance(other, Complex):
                raise IsNotComplex()
        except IsNotComplex as err:
            print(err.txt)
        else:
            return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        """"Умножение комплексных чисел."""
        try:
            if not isinstance(other, Complex):
                raise IsNotComplex()
        except IsNotComplex as err:
            print(err.txt)
        else:
            return Complex(self.real * other.real - self.imaginary * other.imaginary,
                           self.real * other.imaginary + other.real * self.imaginary)


complex_1 = Complex(10, 20)
complex_2 = Complex(2, 6)
complex_3 = complex_1 + complex_2
complex_4 = complex_1 * complex_2

print(f'Первое число {complex_1}')
print(f'Второе число {complex_2}')
print(f'Сумма комплексных чисел {complex_3}')
print(f'Произведение комплексных чисел {complex_4}')
