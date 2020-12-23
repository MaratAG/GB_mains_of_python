"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""


string_count = 0

with open('user_file.txt', 'r') as user_file:
    for line in user_file:
        string_count += 1
        words_count = len(line.split())
        print(f'Строка {string_count} - количество слов: {words_count}')
    print(f'В файле {string_count} строк.')
