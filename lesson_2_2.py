"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

input_list = input('Введите через пробел значения списка: ').strip().split()
output_list = input_list[:]

len_of_output_list = len(output_list)

if len_of_output_list:
    for index in range(0, len_of_output_list - 1, 2):
        output_list[index], output_list[index + 1] = output_list[index + 1], output_list[index]

print('Исходный список {}'.format(input_list))
print('Обработанный список {}'.format(output_list))
