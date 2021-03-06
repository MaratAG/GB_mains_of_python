"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
средней величины дохода сотрудников.
"""


min_wage = 20000
wage_fund = 0
count_employees = 0
file_name = 'wage_file.txt'

try:
    with open(file_name, 'r') as wage_file:
        strings = wage_file.readlines()
except FileNotFoundError:
    print(f'Файл {file_name} не найден!')
else:
    for line in strings:
        wage_data = line.split()

        if len(wage_data) == 2:
            employees = wage_data[0]
            wage = float(wage_data[1])

            wage_fund += wage
            count_employees += 1

            if wage < min_wage:
                print(f'Сотрудник {employees} - {wage:.2f} USD')

    if count_employees:
        print(f'Cредняя величина дохода сотрудников - {wage_fund / count_employees:.2f} USD')
