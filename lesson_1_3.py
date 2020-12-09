"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + n + nnn. Например, пользователь ввел число 3.
Считаем 3 + 33 + 333 = 369.
"""

count_of_elements = 3
users_number = input('Введите число: ').strip()

result_of_calculate = 0
for i in range(1, count_of_elements + 1):
    result_of_calculate += int(i * users_number)

print(result_of_calculate)
