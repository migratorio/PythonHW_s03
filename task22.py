# Задача 22. Найти сумму чисел списка, стоящих на нечётной позиции
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
N = int(input('Введите размер списка: '))
rand_list = []
odd_list = []
summa = 0
j = 0
for i in range(N):
	x = random.randint(1, 10)
	rand_list.append(x)
	if i % 2 != 0:
		summa += x
		odd_list.append(x)
print(rand_list, '-> на нечётных позициях элементы: ', *odd_list, ', cумма = ', summa)
