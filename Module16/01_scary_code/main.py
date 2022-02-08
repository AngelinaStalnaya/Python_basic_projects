main_list = [1, 5, 3]
additional_1 = [1, 5, 1, 5]
additional_2 = [1, 3, 1, 5, 3, 3]
num_5 = 0
num_3 = 0

main_list.extend(additional_1)
num_5 = main_list.count(5)
print('Кол-во цифр 5 при первом объединении:', num_5)

for _ in range(num_5):
    main_list.remove(5)

main_list.extend(additional_2)
num_3 = main_list.count(3)
print('Кол-во цифр 3 при втором объединении:', num_3)
print('Итоговый список: ', main_list)