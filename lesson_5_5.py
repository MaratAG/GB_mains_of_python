"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""


output_file_name = 'output_file_5.txt'

with open(output_file_name, 'w', encoding='utf-8') as output_file:
    numerics = input('Введите набор чисел, разделенных пробелом: ')
    sum_numeric = sum(list(map(int, numerics.split())))
    output_file.write(numerics)
    print(f'Создан файл {output_file_name}')

try:
    with open(output_file_name) as output_file:
        lines = output_file.readlines()
except FileNotFoundError:
    print(f'Не найден файл {output_file_name}!')
else:
    if len(lines):
        sum_numeric = 0
        for line in lines:
            sum_numeric += sum(list(map(int, line.split())))
        print(f'Сумма чисел в файле: {sum_numeric}')
    else:
        print(f'Файл {output_file_name} пуст.')
