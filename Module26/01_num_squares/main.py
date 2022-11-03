from collections.abc import Iterable


class SquareIterator:

    """
    Класс-итератор, создающий итератор возведения чисел от 1
    до number(конечного числа) в квадрат

    """

    def __init__(self, number: int) -> None:
        """
        Метод, инициализирующий класс

        :param number: передаваемое значение является конечным числом
        для возведения в квадрат
        """
        self.list = []
        self.start = 0
        self.stop = number

    def __iter__(self) -> Iterable[int]:
        """
        Метод, создающий итерируемый объект

        :return: объект
        """
        return self

    def __next__(self) -> int:
        """
        Метод, используемый для перехода от текущего числа к следующему числу,
        возводит новое число из последовательности в квадрат

        :return: последующее число в квадрате
        """
        self.start += 1
        if self.start > self.stop:
            raise StopIteration
        else:
            new_num = self.start ** 2
            self.list.append(new_num)
        return new_num


first_iterator = SquareIterator(int(input('Введите число: ')))
for i_value in first_iterator:
    print(i_value, end=' ')
print()


def get_generator(number: int) -> Iterable[int]:
    """
    Генератор возведения числа в квадрат

    :param number: количество чисел в последовательности

    :return: число в квадрате
    """
    for i in range(number):
        yield (i + 1) ** 2


first_generator = get_generator(int(input('Введите число: ')))
for j_val in first_generator:
    print(j_val, end=' ')
print()


second_generator = ((i + 1) ** 2 for i in range(int(input('Введите число: '))))
for c_val in second_generator:
    print(c_val, end=' ')
