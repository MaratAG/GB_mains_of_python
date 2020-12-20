"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
"""

start_number = 20
finish_number = 240
multiple = 20

output_list = [item for item in range(start_number, finish_number) if item % multiple == 0]
print(output_list)
