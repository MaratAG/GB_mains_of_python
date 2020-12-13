"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

users_time = int(input('Введите время в секундах: '))

sec_in_hour = 3600
sec_in_min = 60

seconds_not_in_hours = users_time % sec_in_hour

hours = users_time // sec_in_hour
minutes = seconds_not_in_hours // sec_in_min
seconds = seconds_not_in_hours % sec_in_min

print('Время в формате: {:02}:{:02}:{:02}'.format(hours, minutes, seconds))
