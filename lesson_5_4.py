"""
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""


input_file_name = 'input_number_files.txt'
output_file_name = 'output_number_files.txt'

rus_numerics = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
}

try:
    with open(input_file_name, 'r') as input_file:
        lines = input_file.readlines()
except FileNotFoundError:
    print(f'Не найден файл {input_file_name}!')
else:
    with open(output_file_name, 'w', encoding='utf-8') as output_file:
        for line in lines:
            words = line.split()
            rus_numeric = rus_numerics.get(words[0].lower())
            if rus_numeric is not None:
                words[0] = rus_numeric.title()
                output_file.write(f"{' '.join(words)}\n")
