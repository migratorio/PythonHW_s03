# задача	Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import re

a = input('Введите (через пробел  или запятую) элементы списка в виде вещественных чисел: ')
a_list = re.split('[, ]', a)
a_list = list(map(float, a_list))
el_min = float(a_list[0]) - int(a_list[0])
el_max = a_list[0] - int(a_list[0])
for el in a_list:
	el = el - int(el)
	if el != 0:
		if el < el_min:
			el_min = el
		elif el > el_max:
			el_max = el
print(a_list, '=>', round((el_max - el_min), 2))
