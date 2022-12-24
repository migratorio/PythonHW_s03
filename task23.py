# Задача 23. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент,
#            второй и предпоследний и.т.д
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

a_list =input('Введите через запятую числовые элементы списка: ').split(',')
a_list = [int(x) for x in a_list]
res_list = []
print(a_list, '=> ', end='')
for i in range(0, int(len(a_list) / 2 + 1)):
	a = a_list[i] * a_list[(-i - 1)]
	if len(a_list) % 2 == 0 and i == int(len(a_list)/2):
		break
	res_list.append(a)
print(res_list)
