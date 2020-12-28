"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
"""


input_list = input('Введите элементы исходного списка (через пробел): ').split()
input_list = list(map(int, input_list))
output_list = [input_list[i] for i in range(1, len(input_list)) if input_list[i] > input_list[i - 1]]
print(output_list)
