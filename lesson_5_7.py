"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Итоговый список сохранить в виде json-объекта в соответствующий файл.
"""


import json

output_file_name = 'firms.txt'
json_file_name = 'analytics.json'
analytics = [{}, {'average_profit': .0}]
profit_count = 0

try:
    with open(output_file_name, encoding='utf-8') as output_file:
        lines = output_file.readlines()
except FileNotFoundError:
    print(f'Не найден файл {output_file_name}!')
else:
    firms = analytics[0]
    profit_element = analytics[1]

    if lines:
        for item in lines:
            line = item.split()
            if len(line) == 4:
                key = firms.get(line[0])
                if key is None:
                    key = line[0]
                    firms[key] = 0

                value = float(line[2])
                costs = float(line[3])
                profit = value - costs

                firms[key] = + profit
                profit_element['average_profit'] += 0 if profit < 0 else profit
                profit_count += 0 if profit < 0 else 1

        profit_element['average_profit'] /= 1 if profit_count == 0 else profit_count

with open(json_file_name, 'w') as json_file:
    json.dump(analytics, json_file)
    print(f'Данные записаны в файл {json_file_name}.')
