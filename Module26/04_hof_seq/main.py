from collections.abc import Iterable


def QHofstadter(num_list: list) -> Iterable[int]:
    """
    Генератор поиска последующего числа и формирование последовательности
    чисел Q Хофштадтера
    :param num_list: список из двух чисел: 1 - начальное число последовательности,
    2 - конечное число последовательности
    :return: последовательность чисел
    """
    if num_list == [1, 2]:
        print('Последовательность завершена.')
        return

    def function(number: int) -> int:
        """
        Генератор следующего числа последовательности
        :param number: число, для которого необходимо найти значение
        согласно формуле нахождения в последовательности
        :return: значение числа в последовательности
        """
        if number < 3:
            return 1
        else:
            result = function(number - function(number - 1)) + function(number - function(number - 2))
            return result

    for i in range(num_list[0], num_list[1] + 1):
        yield function(i)


my_function = QHofstadter([1, 10])
for i_number in my_function:
    print(i_number, end=' ')