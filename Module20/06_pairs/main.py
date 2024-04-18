import random

original_list = [random.randint(0, 10) for i in range(10)]
print('Оригинальный список: ', original_list)
print('Новый список: ', [(original_list[part], original_list[part + 1]) for part in range(0, 10, 2)])
print()

my_list = [number for number in range(0, 10)]
print('Оригинальный список: ', my_list)
i_sym = [i_sym for i_sym in my_list if i_sym % 2 == 0]
j_sym = [j_sym for j_sym in my_list if j_sym % 2 != 0]
print('Новый список: ', list(zip(i_sym, j_sym)))

