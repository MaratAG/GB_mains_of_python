"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""


file_name = 'user_file.txt'

try:
    with open(file_name, 'r') as user_file:
        strings = user_file.readlines()
except FileNotFoundError:
    print(f'Файл {file_name} не найден!')
else:
    count = 0
    for line in strings:
        count += 1
        words_count = len(line.strip().split())
        print(f'Строка {count} - количество слов: {words_count}')

    print(f'В файле {len(strings)} строк.')
