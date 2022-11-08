# from collections.abc import Iterable


# def QHofstadter(num_list: list) -> Iterable[int]:
#     """
#     Генератор поиска последующего числа и формирование последовательности
#     чисел Q Хофштадтера
#     :param num_list: список из двух чисел: 1 - начальное число последовательности,
#     2 - конечное число последовательности
#     :return: последовательность чисел
#     """
#     if num_list == [1, 2]:
#         print('Последовательность завершена.')
#         return
#
#     def function(number: int) -> int:
#         """
#         Генератор следующего числа последовательности
#         :param number: число, для которого необходимо найти значение
#         согласно формуле нахождения в последовательности
#         :return: значение числа в последовательности
#         """
#         if number < 3:
#             return 1
#         else:
#             result = function(number - function(number - 1)) + function(number - function(number - 2))
#             return result
#
#     for i in range(num_list[0], num_list[1] + 1):
#         yield function(i)
#
#
# my_function = QHofstadter([1, 10])
# for i_number in my_function:
#     print(i_number, end=' ')


class QHofstadter:

    def __init__(self, num_list: list):
        self.start = num_list[0]
        self.stop = num_list[1]
        self.count = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == 1 and self.stop == 2:
            print('Последовательность закончена.')
            raise StopIteration
        elif self.count < self.stop:
            self.count += 1
            return self.function(self.count)
        else:
            raise StopIteration

    def function(self, number: int):
        if number < 3:
            return 1
        else:
            return self.function(number - self.function(number - 1)) + self.function(number - self.function(number - 2))


my_seq = QHofstadter([1, 20])
print('Последовательность Q Хофштадтера с 1 по 20 позиции:')
for num in my_seq:
    print(num, end=' ')
print('\n')

print('Последовательность Q Хофштадтера с 3 по 16 позиции:')
my_seq_2 = QHofstadter([3, 16])
for i_num in my_seq_2:
    print(i_num, end=' ')

#
# Несколько первых членов этой последовательности
#  1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 6, 8, 8, 8, 10, 9, 10, 11, 11, 12, ...