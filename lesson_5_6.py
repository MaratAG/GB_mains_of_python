"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
 практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не
 обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
 по нему. Вывести словарь на экран.
"""


def get_tasks(hours_of_tasks):
    """
    Рассчитать количество занятий по предмету.

    :param hours_of_tasks: список строк, в которых может быть указано количество занятий.
    :return: общее количество занятий.
    """

    numbers = '1234567890'
    total = 0

    for item in hours_of_tasks:
        hours = ''
        for symbol in item:
            if symbol in numbers:
                hours += symbol
        total += 0 if hours == '' else int(hours)

    return total


output_file_name = 'tasks.txt'
tasks = {}

try:
    with open(output_file_name, encoding='utf-8') as output_file:
        lines = output_file.readlines()
except FileNotFoundError:
    print(f'Не найден файл {output_file_name}!')
else:
    if len(lines):
        for line in lines:
            words = line.strip().split()
            key = tasks.get(words[0])
            if key is None:
                key = words[0]
                tasks[key] = 0
            tasks[key] = + get_tasks(words[1:])
        if tasks:
            print(tasks)

    else:
        print(f'Файл {output_file_name} пуст.')
