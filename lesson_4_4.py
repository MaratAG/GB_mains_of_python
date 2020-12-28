"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор.
"""

input_list = input('Введите список чисел (через пробел): ').split()
input_list = list(map(int, input_list))

number_occurrences = 1

output_list = [item for item in input_list if input_list.count(item) == number_occurrences]
print(output_list)
