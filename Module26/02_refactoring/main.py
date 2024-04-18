from collections.abc import Iterable


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break


def find_numbers(list1: list, list2: list) -> Iterable[int]:
    """
    Генератор - поисковик множителей числа 56
    :param list1: список чисел, содержащих первый множитель
    :param list2: список чисел, содержащих второй множитель
    :return: результат поиска множителей
    """
    for x in list1:
        for y in list2:
            """
            Генератор в генераторе
            """
            result = x * y
            yield f'{x} * {y} = {result}'
            if result == to_find:
                print('Found!!!')
                return


my_result = find_numbers(list_1, list_2)
for i in find_numbers(list_1, list_2):
    print(i)
